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
        
        self.ui.button_0.clicked.connect(self.func_0)
        self.ui.button_1.clicked.connect(self.func_1)
        self.ui.button_2.clicked.connect(self.func_2)
        self.ui.button_3.clicked.connect(self.func_3)
        self.ui.button_4.clicked.connect(self.func_4)
        self.ui.button_5.clicked.connect(self.func_5)
        self.ui.button_6.clicked.connect(self.func_6)
        self.ui.button_7.clicked.connect(self.func_7)
        self.ui.button_8.clicked.connect(self.func_8)
        self.ui.button_9.clicked.connect(self.func_9)
        self.ui.button_dot.clicked.connect(self.func_dot)
        
        self.ui.button_AC.clicked.connect(self.func_AC)
        self.ui.button_C.clicked.connect(self.func_C)
        self.ui.button_changeSign.clicked.connect(self.func_chanegSign)
        self.ui.button_power.clicked.connect(self.func_power)
        
        self.ui.button_div.clicked.connect(self.func_div)
        self.ui.button_multi.clicked.connect(self.func_multi)
        self.ui.button_sub.clicked.connect(self.func_sub)
        self.ui.button_sum.clicked.connect(self.func_sum)
        self.ui.button_equal.clicked.connect(self.func_equal)
        
        self.ui.button_sqrt.clicked.connect(self.func_sqrt)
        self.ui.button_log.clicked.connect(self.func_log)
        self.ui.button_sin.clicked.connect(self.func_sin)
        self.ui.button_cos.clicked.connect(self.func_cos)
        self.ui.button_tan.clicked.connect(self.func_tan)
        self.ui.button_cot.clicked.connect(self.func_cot)
        
    def func_0(self):
        self.ui.textbox.setText(self.ui.textbox.text() + '0')
    def func_1(self):
        self.ui.textbox.setText(self.ui.textbox.text() + '1')
    def func_2(self):
        self.ui.textbox.setText(self.ui.textbox.text() + '2')
    def func_3(self):
        self.ui.textbox.setText(self.ui.textbox.text() + '3')
    def func_4(self):
        self.ui.textbox.setText(self.ui.textbox.text() + '4')
    def func_5(self):
        self.ui.textbox.setText(self.ui.textbox.text() + '5')
    def func_6(self):
        self.ui.textbox.setText(self.ui.textbox.text() + '6')
    def func_7(self):
        self.ui.textbox.setText(self.ui.textbox.text() + '7')
    def func_8(self):
        self.ui.textbox.setText(self.ui.textbox.text() + '8')
    def func_9(self):
        self.ui.textbox.setText(self.ui.textbox.text() + '9')
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
    def func_power(self):
        try:
            self.first_number = int(self.ui.textbox.text())
            self.ui.textbox.setText('')
            self.sign = 'power'
        except:
            try:
                self.first_number = float(self.ui.textbox.text())
                self.ui.textbox.setText('')
                self.sign = 'power'
            except:
                pass
    
    def func_div(self):
        try:
            self.first_number = int(self.ui.textbox.text())
            self.ui.textbox.setText('')
            self.sign = 'div'
        except:
            try:
                self.first_number = float(self.ui.textbox.text())
                self.ui.textbox.setText('')
                self.sign = 'div'
            except:
                pass
    def func_multi(self):
        try:
            self.first_number = int(self.ui.textbox.text())
            self.ui.textbox.setText('')
            self.sign = 'multi'
        except:
            try:
                self.first_number = float(self.ui.textbox.text())
                self.ui.textbox.setText('')
                self.sign = 'multi'
            except:
                pass
    def func_sub(self):
        try:
            self.first_number = int(self.ui.textbox.text())
            self.ui.textbox.setText('')
            self.sign = 'sub'
        except:
            try:
                self.first_number = float(self.ui.textbox.text())
                self.ui.textbox.setText('')
                self.sign = 'sub'
            except:
                pass
    def func_sum(self):
        try:
            self.first_number = int(self.ui.textbox.text())
            self.ui.textbox.setText('')
            self.sign = 'sum'
        except:
            try:
                self.first_number = float(self.ui.textbox.text())
                self.ui.textbox.setText('')
                self.sign = 'sum'
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
    
    def func_sqrt(self):
        try:
            self.ui.textbox.setText(str(math.sqrt(int(self.ui.textbox.text()))))
        except:
            try:
                self.ui.textbox.setText(str(math.sqrt(float(self.ui.textbox.text()))))
            except:
                pass
    def func_log(self):
        try:
            self.ui.textbox.setText(str(math.log(int(self.ui.textbox.text()))))
        except:
            try:
                self.ui.textbox.setText(str(math.log(float(self.ui.textbox.text()))))
            except:
                pass
    def func_sin(self):
        try:
            self.ui.textbox.setText(str(math.sin(math.radians(int(self.ui.textbox.text())))))
        except:
            try:
                self.ui.textbox.setText(str(math.sin(math.radians(float(self.ui.textbox.text())))))
            except:
                pass
    def func_cos(self):
        try:
            self.ui.textbox.setText(str(math.cos(math.radians(int(self.ui.textbox.text())))))
        except:
            try:
                self.ui.textbox.setText(str(math.cos(math.radians(float(self.ui.textbox.text())))))
            except:
                pass
    def func_tan(self):
        try:
            self.ui.textbox.setText(str(math.tan(math.radians(int(self.ui.textbox.text())))))
        except:
            try:
                self.ui.textbox.setText(str(math.tan(math.radians(float(self.ui.textbox.text())))))
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
    
app = QApplication([])
window = Calculator()
app.exec()