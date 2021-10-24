from functools import partial
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *
import database

class TODO(QMainWindow):
    def __init__(self):
        super().__init__()
        
        loader = QUiLoader()
        self.ui = loader.load('form.ui', None)        
        self.ui.show()
        
        self.ui.btn.clicked.connect(self.addNewTaskToDatabase)
        self.readFromDatabase()
        
    def addNewTaskToDatabase(self):
        title = self.ui.line_title.text()
        done = '0'
        description = self.ui.line_description.text()
        if self.ui.combo.currentText() == "Important":
            priority = '1'
        elif self.ui.combo.currentText() == "Unimportant":
            priority = '0'
        date = self.ui.line_date.text()
        time = self.ui.line_time.text()
        
        if title == '':
            msg = QMessageBox()
            msg.setText('The title should not be empty!')
            msg.setIcon(QMessageBox.Warning)
            msg.exec()
        else:
            database.add(title, done, description, priority, date, time)
        
            self.readFromDatabase()
            
            self.ui.line_title.setText('')
            self.ui.line_description.setText('')
            self.ui.line_date.setText('')
            self.ui.line_time.setText('')
        
    def readFromDatabase(self):
        results = database.getAll()
        
        for i in range(len(results)):
            self.new_lbl_title = QLabel()
            self.new_btn_delete = QPushButton()
            self.new_btn_info = QPushButton()
            self.new_check = QCheckBox()
            self.new_btn_do = QPushButton()
            self.new_btn_undo = QPushButton()
            
            # Style Sheets
            self.new_btn_info.setText('❓')
            self.new_btn_info.setStyleSheet('border: 1px solid white; background-color: white; font-size: 13px; padding: 5px 5px;')
            self.new_lbl_title.setText(results[i][1])
            if results[i][4] == '1':
                self.new_lbl_title.setStyleSheet('color: #C71585; font-size: 20px; border: 2px solid #ADD8E6; border-radius: 12px;')
            else:
                self.new_lbl_title.setStyleSheet('color: #48D1CC; font-size: 17px; border: 2px solid #ADD8E6; border-radius: 12px;')
            self.new_btn_do.setText('✔')
            self.new_btn_do.setStyleSheet('border: 1px solid white; background-color: #F0FFFF; color: green; font-size: 22px; padding: 5px 5px;')
            self.new_btn_undo.setText('🔘')
            self.new_btn_undo.setStyleSheet('border: 1px solid white; background-color: #FDF5E6; color: green; font-size: 15px; padding: 5px 5px;')
            self.new_btn_delete.setText('❌')
            self.new_btn_delete.setStyleSheet('border: 1px solid white; background-color: white; font-size: 18px; padding: 5px 5px;')
            
            if results[i][2] == '0':
                self.ui.gridLayout_remain.addWidget(self.new_btn_info, i, 0)
                self.new_btn_info.clicked.connect(partial(self.info, results[i]))
                self.ui.gridLayout_remain.addWidget(self.new_lbl_title, i, 1)
                self.ui.gridLayout_remain.addWidget(self.new_btn_do, i, 2)
                self.new_btn_do.clicked.connect(partial(self.do, results[i], self.new_btn_info, self.new_lbl_title, self.new_btn_do, self.new_check, self.new_btn_delete))
                self.ui.gridLayout_remain.addWidget(self.new_check, i, 3)
                self.new_check.setChecked(False)
                self.ui.gridLayout_remain.addWidget(self.new_btn_delete, i, 4)
                self.new_btn_delete.clicked.connect(partial(self.remove, results[i], self.new_btn_info, self.new_lbl_title, self.new_btn_do, self.new_check, self.new_btn_delete))
                
            elif results[i][2] == '1':
                self.ui.gridLayout_done.addWidget(self.new_btn_info, i, 0)
                self.new_btn_info.clicked.connect(partial(self.info, results[i]))
                self.ui.gridLayout_done.addWidget(self.new_lbl_title, i, 1)
                self.ui.gridLayout_done.addWidget(self.new_btn_undo, i, 2)
                self.new_btn_undo.clicked.connect(partial(self.undo, results[i], self.new_btn_info, self.new_lbl_title, self.new_btn_undo, self.new_check, self.new_btn_delete))
                self.ui.gridLayout_done.addWidget(self.new_check, i, 3)
                self.new_check.setChecked(True)
                self.ui.gridLayout_done.addWidget(self.new_btn_delete, i, 4)
                self.new_btn_delete.clicked.connect(partial(self.remove, results[i], self.new_btn_info, self.new_lbl_title, self.new_btn_undo, self.new_check, self.new_btn_delete))
    
    def info(self, i):
        msg = QMessageBox()
        msg.setWindowTitle('Work Information')
        msg.setText(f'Title = {i[1]}\nDescription = {i[3]}\nPriority = {i[4]}\nDate = {i[5]}\nTime = {i[6]}')
        msg.setIcon(QMessageBox.Information)
        msg.exec()
        
    def remove(self, i, btn_info, lbl_title, btn_do, check, btn_delete):
        database.remove(i[1])
        btn_info.deleteLater()
        lbl_title.deleteLater()
        btn_do.deleteLater()
        check.deleteLater()
        btn_delete.deleteLater()
        msg = QMessageBox()
        msg.setWindowTitle('❗')
        msg.setText("Removed without any problems")
        msg.exec()
    
    def do(self, i, btn_info, lbl_title, btn_do, check, btn_delete):
        if check.isChecked() == True:
            database.updateDo(i[1])
            self.readFromDatabase()
            btn_info.deleteLater()
            lbl_title.deleteLater()
            btn_do.deleteLater()
            check.deleteLater()
            btn_delete.deleteLater()
            msg = QMessageBox()
            msg.setText("Work Changed :)")
            msg.exec()
        else:
            msg = QMessageBox()
            msg.setText("Work Not Changed :(")
            msg.exec()
    
    def undo(self, i, btn_info, lbl_title, btn_do, check, btn_delete):
        if check.isChecked() == False:
            database.updateUndo(i[1])
            self.readFromDatabase()
            btn_info.deleteLater()
            lbl_title.deleteLater()
            btn_do.deleteLater()
            check.deleteLater()
            btn_delete.deleteLater()
            msg = QMessageBox()
            msg.setText("Work Changed :)")
            msg.exec()
        else:
            msg = QMessageBox()
            msg.setText("Work Not Changed :(")
            msg.exec()
            
app = QApplication([])
window = TODO()
app.exec()