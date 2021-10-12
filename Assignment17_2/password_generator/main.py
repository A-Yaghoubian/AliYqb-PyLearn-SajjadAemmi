import string
import random
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *

class PasswordGenerator(QMainWindow):
    def __init__(self):
        super().__init__()
        
        loader = QUiLoader()
        self.ui = loader.load('form.ui', None)
        self.ui.show()
        
        self.pass_char = string.printable[:95]
                
        self.ui.btn_simple.clicked.connect(self.simple)
        self.ui.btn_good.clicked.connect(self.good)
        self.ui.btn_strong.clicked.connect(self.strong)
        self.ui.btn_superStrong.clicked.connect(self.superStrong)
    
    def simple(self):
        self.ui.line_simple.setText('')
        self.password = random.choices(self.pass_char, k=4)
        self.ui.line_simple.setText(''.join(self.password))
    
    def good(self):
        self.ui.line_good.setText('')
        self.password = random.choices(self.pass_char, k=8)
        self.ui.line_good.setText(''.join(self.password))
    
    def strong(self):
        self.ui.line_strong.setText('')
        self.password = random.choices(self.pass_char, k=12)
        self.ui.line_strong.setText(''.join(self.password))
    
    def superStrong(self):
        self.ui.line_superStrong.setText('')
        self.password = random.choices(self.pass_char, k=20)
        self.ui.line_superStrong.setText(''.join(self.password))

app = QApplication([])
window = PasswordGenerator()
app.exec()