from random import randint
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtUiTools import QUiLoader

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        loader = QUiLoader()
        self.ui = loader.load('main.ui', None)
        
        self.game = [[None for i in range(9)] for j in range(9)]
        
        for i in range(9):
            for j in range(9):
                tb = QLineEdit()
                tb.setStyleSheet('font-size: 32px;')
                tb.setAlignment(Qt.AlignCenter)
                tb.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
                self.game[i][j] = tb
                self.game[i][j].textChanged.connect(self.checkGame)
                self.ui.gridLayout.addWidget(tb, i, j)
        
        self.ui.show()    
        
        self.ui.btn_darkMode.clicked.connect(self.darkMode)
        self.ui.btn_newGame.clicked.connect(self.newGame)
        self.ui.btn_checkGame.clicked.connect(self.checkGame)
        
    def checkGame(self):
        self.win_flag = True
        for row in range(9):
            for i in range(9):
                for j in range(9):
                    if self.game[row][i].text() == self.game[row][j].text() and i != j and self.game[row][i].text() != '':
                        self.game[row][i].setStyleSheet('font-size: 32px; color: red')
                        self.win_flag = False
        
        for col in range(9):
            for i in range(9):
                for j in range(9):
                    if self.game[i][col].text() == self.game[j][col].text() and i != j and self.game[i][col].text() != '':
                        self.game[i][col].setStyleSheet('font-size: 32px; color: red')
                        self.win_flag = False
                        
        for row in range(0, 3):
            for col in range(0, 3):
                for r in range(0, 3):
                    for c in range(0, 3):
                        if self.game[r][c].text() == self.game[row][col].text() and self.game[row][col].text() != '' and row != r and col != c:
                            self.game[row][col].setStyleSheet('font-size: 32px; color: red')
                            self.win_flag = False
            for col in range(3, 6):
                for r in range(0, 3):
                    for c in range(3, 6):
                        if self.game[r][c].text() == self.game[row][col].text() and self.game[row][col].text() != '' and row != r and col != c:
                            self.game[row][col].setStyleSheet('font-size: 32px; color: red')
                            self.win_flag = False
            for col in range(6, 9):
                for r in range(0, 3):
                    for c in range(6, 9):
                        if self.game[r][c].text() == self.game[row][col].text() and self.game[row][col].text() != '' and row != r and col != c:
                            self.game[row][col].setStyleSheet('font-size: 32px; color: red')
                            self.win_flag = False
                            
        for row in range(3, 6):
            for col in range(0, 3):
                for r in range(3, 6):
                    for c in range(0, 3):
                        if self.game[r][c].text() == self.game[row][col].text() and self.game[row][col].text() != '' and row != r and col != c:
                            self.game[row][col].setStyleSheet('font-size: 32px; color: red')
                            self.win_flag = False
            for col in range(3, 6):
                for r in range(3, 6):
                    for c in range(3, 6):
                        if self.game[r][c].text() == self.game[row][col].text() and self.game[row][col].text() != '' and row != r and col != c:
                            self.game[row][col].setStyleSheet('font-size: 32px; color: red')
                            self.win_flag = False
            for col in range(6, 9):
                for r in range(3, 6):
                    for c in range(6, 9):
                        if self.game[r][c].text() == self.game[row][col].text() and self.game[row][col].text() != '' and row != r and col != c:
                            self.game[row][col].setStyleSheet('font-size: 32px; color: red')
                            self.win_flag = False
                            
        for row in range(6, 9):
            for col in range(0, 3):
                for r in range(6, 9):
                    for c in range(0, 3):
                        if self.game[r][c].text() == self.game[row][col].text() and self.game[row][col].text() != '' and row != r and col != c:
                            self.game[row][col].setStyleSheet('font-size: 32px; color: red')
                            self.win_flag = False
            for col in range(3, 6):
                for r in range(6, 9):
                    for c in range(3, 6):
                        if self.game[r][c].text() == self.game[row][col].text() and self.game[row][col].text() != '' and row != r and col != c:
                            self.game[row][col].setStyleSheet('font-size: 32px; color: red')
                            self.win_flag = False
            for col in range(6, 9):
                for r in range(6, 9):
                    for c in range(6, 9):
                        if self.game[r][c].text() == self.game[row][col].text() and self.game[row][col].text() != '' and row != r and col != c:
                            self.game[row][col].setStyleSheet('font-size: 32px; color: red')
                            self.win_flag = False
            
        for row in range(0, 9):
            for col in range(0, 9):
                if self.game[row][col].text() == '':
                    self.win_flag = False
        
        if self.win_flag == True:
            win_messageBox = QMessageBox()
            win_messageBox.setText('Congratulations 🎊 You are winner 🏆')
            win_messageBox.exec()
            
                        

        
    def newGame(self):
        for i in range(9):
            for j in range(9):
                self.game[i][j].setText('')
        
        try:
            r = randint(1, 6)
            file_path = f'data/s{r}.txt'
            
            f = open(file_path, 'r')
            big_text = f.read()
            rows = big_text.split('\n')
            for i in range(9):
                numbers = rows[i].split(' ')
                for j in range(9):
                    if(numbers[j] != '0'):
                        self.game[i][j].setStyleSheet('font-size: 32px; color: black')
                        self.game[i][j].setText(numbers[j])
                        self.game[i][j].setReadOnly(True)
                    else:
                        self.game[i][j].setStyleSheet('font-size: 32px; color: skyBlue')
                        self.game[i][j].setReadOnly(False)        
        
        except:
            warning_messageBox = QMessageBox()
            warning_messageBox.setText('Please check your numbers files 👀')
            warning_messageBox.exec()
        
    def darkMode(self):
        if self.ui.btn_darkMode.text() == 'Dark Mode':
            self.ui.setStyleSheet('background-color: rgb(91, 91, 91);')
            self.ui.btn_darkMode.setText('Light Mode')
            
        else:
            self.ui.setStyleSheet('background-color: rgb(227, 239, 244);')
            self.ui.btn_darkMode.setText('Dark Mode')
        
app = QApplication([])
window = MainWindow()
app.exec()