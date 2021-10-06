import random
from functools import partial
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *

class TicTacToe(QMainWindow):
    def __init__(self):
        super().__init__()
        
        loader = QUiLoader()
        self.ui = loader.load('form.ui', None)
        self.ui.show()
        
        self.game = [[self.ui.button_1, self.ui.button_2, self.ui.button_3],
                     [self.ui.button_4, self.ui.button_5, self.ui.button_6],
                     [self.ui.button_7, self.ui.button_8, self.ui.button_9]]
        
        self.round = 'X'
        self.pointX = 0
        self.pointO = 0
        self.pointDraw = 0
        self.ui.radio_2.setChecked(True)
        
        self.scoreBoard()
        
        for i in range(3):
            for j in range(3):    
                self.game[i][j].setText('')
                self.game[i][j].setStyleSheet('color: black; background-color: skyblue; border-radius: 40px;')   
                self.game[i][j].clicked.connect(partial(self.play, i, j))
        
        self.ui.button_new.clicked.connect(self.newGame)
        self.ui.button_about.clicked.connect(self.about)
    
    def play(self, i, j):
        if self.game[i][j].text() == '':
            
            if self.round == 'X':
                    self.game[i][j].setStyleSheet('color: green; background-color: lightgreen; border-radius: 20px;')
                    self.game[i][j].setText('X') 
                    self.round = 'O'
                    
                    self.check()
                    
                    if self.ui.radio_cpu.isChecked():
                        if self.round == 'O':
                            while True:
                                i = random.randint(0,2)
                                j = random.randint(0,2)
                                if self.game[i][j].text() == '':
                                    self.game[i][j].setStyleSheet('color: red; background-color: pink; border-radius: 60px;')
                                    self.game[i][j].setText('O')
                                    self.round = 'X'
                                    break        
                                         
            else:
                if self.ui.radio_2.isChecked():
                    self.game[i][j].setStyleSheet('color: red; background-color: pink; border-radius: 60px;')
                    self.game[i][j].setText('O')
                    self.round = 'X'
    
        self.check()
    
    def check(self):
        end_game = False
        
        for i in range(3):
            if (self.game[i][0].text() == 'X' and self.game[i][1].text() == 'X' and self.game[i][2].text() == 'X') or (self.game[0][i].text() == 'X' and self.game[1][i].text() == 'X' and self.game[2][i].text() == 'X') or (self.game[0][0].text() == 'X' and self.game[1][1].text() == 'X' and self.game[2][2].text() == 'X') or (self.game[0][2].text() == 'X' and self.game[1][1].text() == 'X' and self.game[2][0].text() == 'X'):
                msgBox = QMessageBox()
                msgBox.setText('Player 1 wins :)')
                msgBox.setStyleSheet('color: green; background-color: gray;')
                msgBox.exec()
                self.pointX += 1
                self.scoreBoard()
                self.newGame()
                end_game = True
                break
            
            if (self.game[i][0].text() == 'O' and self.game[i][1].text() == 'O' and self.game[i][2].text() == 'O') or (self.game[0][i].text() == 'O' and self.game[1][i].text() == 'O' and self.game[2][i].text() == 'O') or (self.game[0][0].text() == 'O' and self.game[1][1].text() == 'O' and self.game[2][2].text() == 'O') or (self.game[0][2].text() == 'O' and self.game[1][1].text() == 'O' and self.game[2][0].text() == 'O'):
                msgBox = QMessageBox()
                msgBox.setText('Player 2 wins :)')
                msgBox.setStyleSheet('color: red; background-color: gray;')
                msgBox.exec()
                self.pointO += 1
                self.scoreBoard()
                self.newGame()
                end_game = True
                break
            
        counter = 0
        for i in range(3):
            for j in range(3):
                if self.game[i][j].text() == 'O' or self.game[i][j].text() == 'X':
                    counter += 1
                    
        if counter == 9 and end_game == False:
            msgBox = QMessageBox()
            msgBox.setText('Draw :|')
            msgBox.setStyleSheet('color: white; background-color: gray;')
            msgBox.exec()
            self.pointDraw += 1
            self.scoreBoard()
            self.newGame()
            end_game = True
                
    def newGame(self):
        for i in range(3):
            for j in range(3):
                self.game[i][j].setText('')
                self.game[i][j].setStyleSheet('color: black; background-color: skyblue; border-radius: 40px;')

    def about(self):
        msgBox = QMessageBox()
        msgBox.setText('Tic-Tac-Toe game\nYou can play with your friend or computer\nThis game programmed with Python and Qt\nProgrammer: Ali Yaghoubian')
        msgBox.setStyleSheet('color: white; background-color: black;')
        msgBox.exec()
    
    def scoreBoard(self):
        self.ui.line_x.setText(str(self.pointX))
        self.ui.line_o.setText(str(self.pointO))
        self.ui.line_draw.setText(str(self.pointDraw))

app = QApplication([])
window = TicTacToe()
app.exec() 