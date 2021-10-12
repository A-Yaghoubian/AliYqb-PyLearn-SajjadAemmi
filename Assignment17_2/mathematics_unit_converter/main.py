from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *

class Converter(QMainWindow):
    def __init__(self):
        super().__init__()
        
        loader = QUiLoader()
        self.ui = loader.load('form.ui', None)
        
        self.ui.show()
        
        self.ui.btn_convertM.clicked.connect(self.convertM)
        self.ui.btn_convertL.clicked.connect(self.convertL)
        self.ui.btn_convertT.clicked.connect(self.convertT)
        self.ui.btn_convertD.clicked.connect(self.convertD)
        
    def convertM(self):
        try:
            fromM = self.ui.combo_fromM.currentText()
            toM = self.ui.combo_toM.currentText()
            inp = float(self.ui.line_inputM.text())
            self.ui.line_outputM.setText('')
            
            if fromM == 'Gram':
                inp = inp
            elif fromM == 'Kilogram':
                inp = inp * 1000
            elif fromM == 'Ton':
                inp = inp * 1000000 
            elif fromM == 'Pound':
                inp = inp * 453
            
            if toM == 'Gram':
                outp = inp
            elif toM == 'Kilogram':
                outp = inp / 1000
            elif toM == 'Ton':
                outp = inp / 1000000 
            elif toM == 'Pound':
                outp = inp / 453
                
            self.ui.line_outputM.setText(str(outp))
        
        except:
            print('errorM')
            pass
        
    def convertL(self):
        try:
            fromL = self.ui.combo_fromL.currentText()
            toL = self.ui.combo_toL.currentText()
            inp = float(self.ui.line_inputL.text())
            self.ui.line_outputL.setText('')
            
            if fromL == 'Millimetre':
                inp = inp
            elif fromL == 'Centimeter':
                inp = inp * 10
            elif fromL == 'Meter':
                inp = inp * 1000 
            elif fromL == 'Kilometre':
                inp = inp * 1000000
            elif fromL == 'Inch':
                inp = inp * 25.4
            
            if toL == 'Millimetre':
                outp = inp
            elif toL == 'Centimeter':
                outp = inp / 10
            elif toL == 'Meter':
                outp = inp / 1000
            elif toL == 'Kilometre':
                outp = inp / 1000000
            elif toL == 'Inch':
                outp = inp / 25.4
                
            self.ui.line_outputL.setText(str(outp))
        
        except:
            print('errorL')
            pass

    def convertT(self):
        try:
            fromT = self.ui.combo_fromT.currentText()
            toT = self.ui.combo_toT.currentText()
            inp = float(self.ui.line_inputT.text())
            self.ui.line_outputT.setText('')
            
            if fromT == 'Celsius':
                inp = inp
            elif fromT == 'Fahrenheit':
                inp = ((inp - 32) * 5) / 9
            elif fromT == 'Kelvin':
                inp = inp - 273.15
            
            if toT == 'Celsius':
                outp = inp
            elif toT == 'Fahrenheit':
                outp = ((inp * 9) / 5) + 32
            elif toT == 'Kelvin':
                outp = inp + 273.15
                
            self.ui.line_outputT.setText(str(outp))
        
        except:
            print('errorT')
            pass

    def convertD(self):
        try:
            fromD = self.ui.combo_fromD.currentText()
            toD = self.ui.combo_toD.currentText()
            inp = int(self.ui.line_inputD.text())
            self.ui.line_outputD.setText('')
            
            if fromD == 'Bit':
                inp = inp
            elif fromD == 'Byte':
                inp = inp * 8
            elif fromD == 'Kilobyte':
                inp = inp * 8000
            elif fromD == 'Megabyte':
                inp = inp * 8000000
            elif fromD == 'Gigabyte':
                inp = inp * 8000000000
            elif fromD == 'Terabyte':
                inp = inp * 8000000000000
            
            if toD == 'Bit':
                outp = inp
            elif toD == 'Byte':
                outp = inp / 8
            elif toD == 'Kilobyte':
                outp = inp / 8000 
            elif toD == 'Megabyte':
                outp = inp / 8000000
            elif toD == 'Gigabyte':
                outp = inp / 8000000000
            elif toD == 'Terabyte':
                outp = inp / 8000000000000
                
                
            self.ui.line_outputD.setText(str(outp))
        
        except:
            print('errorD')
            pass

app = QApplication([])
window = Converter()
app.exec()