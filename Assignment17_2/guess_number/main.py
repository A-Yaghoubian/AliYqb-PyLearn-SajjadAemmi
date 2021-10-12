from random import randint
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *

class GuessNumber(QMainWindow):
    def __init__(self):
        super().__init__()
        
        loader = QUiLoader()
        self.ui = loader.load('form.ui', None)
        self.ui.show()
        
        self.ui.pushButton_generate.clicked.connect(self.generate)
        self.ui.pushButton_go.clicked.connect(self.go)
        
    def generate(self):
        self.first_number = self.ui.lineEdit_first.text().strip()
        self.last_number = self.ui.lineEdit_last.text().strip()
        
        try:
            if (self.first_number != '' and self.last_number != ''):
                self.random_number = randint(int(self.first_number), int(self.last_number))
        except:
            self.ui.lineEdit_first.setText('')
            self.first_number = ''
            self.ui.lineEdit_last.setText('')
            self.last_number = ''
        
    def go(self):
        self.guess = self.ui.lineEdit_guess.text().strip()
        try:
            if (self.guess != ''):
                if (int(self.guess) > self.random_number):
                    self.ui.lineEdit_hint.setText('Lower 🔽')
                elif (int(self.guess) < self.random_number):
                    self.ui.lineEdit_hint.setText('Upper 🔼')
                else:
                    self.ui.lineEdit_hint.setText("That's right 💥")
        except:
            if (self.first_number != '' and self.last_number != ''):
                self.ui.lineEdit_guess.setText('')
                self.guess = ''
                self.ui.lineEdit_hint.setText('')
            else:
                pass
        
app = QApplication([])
window = GuessNumber()
app.exec()