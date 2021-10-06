from functools import partial
import math
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        
        loader = QUiLoader()
        self.ui = loader.load('example.ui', None)
        self.ui.show()
        
        self.ui.button_0.clicked.connect(partial(self.func_numbers, '0'))
        self.ui.button_1.clicked.connect(partial(self.func_numbers, '1'))
        self.ui.button_2.clicked.connect(partial(self.func_numbers, '2'))
        self.ui.button_3.clicked.connect(partial(self.func_numbers, '3'))
        self.ui.button_4.clicked.connect(partial(self.func_numbers, '4'))
        self.ui.button_5.clicked.connect(partial(self.func_numbers, '5'))
        self.ui.button_6.clicked.connect(partial(self.func_numbers, '6'))
        self.ui.button_7.clicked.connect(partial(self.func_numbers, '7'))
        self.ui.button_8.clicked.connect(partial(self.func_numbers, '8'))
        self.ui.button_9.clicked.connect(partial(self.func_numbers, '9'))
        
        self.ui.button_dot.clicked.connect(self.func_dot)
        self.ui.button_AC.clicked.connect(self.func_AC)
        self.ui.button_C.clicked.connect(self.func_C)
        self.ui.button_changeSign.clicked.connect(self.func_chanegSign)
        
        self.ui.button_power.clicked.connect(partial(self.func_basic, 'power'))
        self.ui.button_div.clicked.connect(partial(self.func_basic, 'div'))
        self.ui.button_multi.clicked.connect(partial(self.func_basic, 'multi'))
        self.ui.button_sub.clicked.connect(partial(self.func_basic, 'sub'))
        self.ui.button_sum.clicked.connect(partial(self.func_basic, 'sum'))
        
        self.ui.button_equal.clicked.connect(self.func_equal)
        
        self.ui.button_sqrt.clicked.connect(partial(self.func_adv, math.sqrt))
        self.ui.button_log.clicked.connect(partial(self.func_adv, math.log))
        self.ui.button_sin.clicked.connect(partial(self.func_advance, math.sin))
        self.ui.button_cos.clicked.connect(partial(self.func_advance, math.cos))
        self.ui.button_tan.clicked.connect(partial(self.func_advance, math.tan))
        
        self.ui.button_cot.clicked.connect(self.func_cot)
        
    def func_numbers(self, num):
        self.ui.textbox.setText(self.ui.textbox.text() + num)
        
    def func_dot(self):
        if self.ui.textbox.text() == '':
            self.ui.textbox.setText('0.')
        if '.' not in self.ui.textbox.text(): 
            self.ui.textbox.setText(self.ui.textbox.text() + '.') 
    def func_AC(self):
        self.ui.textbox.setText('')
    def func_C(self):
        try:
            self.ui.textbox.setText(self.ui.textbox.text()[:-1])
        except:
            pass
    def func_chanegSign(self):
        try:
            self.ui.textbox.setText(str(int(self.ui.textbox.text()) * -1))
        except:
            try:
                self.ui.textbox.setText(str(float(self.ui.textbox.text()) * -1))
            except:
                pass
            
    def func_basic(self, function):
        try:
            self.first_number = int(self.ui.textbox.text())
            self.ui.textbox.setText('')
            self.sign = function
        except:
            try:
                self.first_number = float(self.ui.textbox.text())
                self.ui.textbox.setText('')
                self.sign = function
            except:
                pass
    
    def func_equal(self):
        try:
            self.second_number = int(self.ui.textbox.text())
        except:
            try:
                self.second_number = float(self.ui.textbox.text())
            except:
                pass
        
        try:
            if self.sign == 'power':
                answer = pow(self.first_number, self.second_number)
                self.sign = ''
            if self.sign == 'div':
                try:
                    answer = self.first_number / self.second_number
                except ZeroDivisionError:
                    answer = 0
                self.sign = ''
            if self.sign == 'multi':
                answer = self.first_number * self.second_number
                self.sign = ''
            if self.sign == 'sub':
                answer = self.first_number - self.second_number
                self.sign = ''
            if self.sign == 'sum':
                answer = self.first_number + self.second_number
                self.sign = ''
        except:
            pass
            
        try:
            self.ui.textbox.setText(str(answer))
        except:
            pass
            
    def func_adv(self, function): # log and sqrt
        try:
            self.ui.textbox.setText(str(function(int(self.ui.textbox.text()))))
        except:
            try:
                self.ui.textbox.setText(str(function(float(self.ui.textbox.text()))))
            except:
                pass
            
    def func_cot(self):
        try:    
            answer = math.cos(math.radians(int(self.ui.textbox.text()))) / math.sin(math.radians(int(self.ui.textbox.text())))
        except:
            try:
                answer = math.cos(math.radians(float(self.ui.textbox.text()))) / math.sin(math.radians(float(self.ui.textbox.text())))
            except:
                pass
        
        try:
            self.ui.textbox.setText(str(answer))
        except:
            pass
        
    def func_advance(self, function): # sin and cos and tan 
        try:
            self.ui.textbox.setText(str(function(math.radians(int(self.ui.textbox.text())))))
        except:
            try:
                self.ui.textbox.setText(str(function(math.radians(float(self.ui.textbox.text())))))
            except:
                pass
    
app = QApplication([])
window = Calculator()
app.exec()