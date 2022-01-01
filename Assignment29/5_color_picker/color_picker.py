from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        loader = QUiLoader()
        self.ui = loader.load("5_color_picker/form.ui", None)
        
        self.ui.show()

        self.ui.red_horizontalSlider.valueChanged.connect(self.action)
        self.ui.green_horizontalSlider.valueChanged.connect(self.action)
        self.ui.blue_horizontalSlider.valueChanged.connect(self.action)
        
    def action(self):
        b = str(self.ui.blue_horizontalSlider.value())
        self.ui.blue_value.setText(b)
        
        g = str(self.ui.green_horizontalSlider.value())
        self.ui.green_value.setText(g)
        
        r = str(self.ui.red_horizontalSlider.value())
        self.ui.red_value.setText(r)
        
        # sum = int(r) + int(g) + int(b)
        # if sum > 372:
        #     self.ui.final_color.setStyleSheet('color: rgb(120, 120, 120);')
        # else:
        #     self.ui.final_color.setStyleSheet('color: rgb(255, 255, 255);')

        self.ui.final_color.setStyleSheet(f'background-color: rgb({r}, {g}, {b});')
        self.ui.final_color.setText(f'rgb({r}, {g}, {b})')


app = QApplication([])
window = MainWindow()
app.exec()