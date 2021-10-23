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
        
        self.ui.btn_add.clicked.connect(self.addNewTaskToDatabase)
        self.readFromDatabase()
        
    def addNewTaskToDatabase(self):
        title = self.ui.tb_title.text()
        description = self.ui.tb_description.text()
        
        database.add(title, description)
        
        self.readFromDatabase()
        
        self.ui.tb_title.setText('')
        self.ui.tb_description.setText('')
        
    def readFromDatabase(self):
        results = database.getAll()
        
        for i in range(len(results)):
            new_checkbox = QCheckBox()
            if (results[i][2] == 1):
                new_checkbox.setChecked(True)                
            
            new_label = QLabel()
            new_label.setText(results[i][1])
            
            new_deleteBtn = QPushButton()
            new_deleteBtn.setText('❌')
            
            self.ui.gridLayout.addWidget(new_checkbox, i, 0)
            self.ui.gridLayout.addWidget(new_label, i, 1)
            self.ui.gridLayout.addWidget(new_deleteBtn, i, 2)
            
app = QApplication([])
window = TODO()
app.exec()