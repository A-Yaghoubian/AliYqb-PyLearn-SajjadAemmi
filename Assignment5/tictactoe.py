import random
from colorama import Fore
import time

def show_game():
    for i in range(3):
        for j in range(3):
            g = game[i][j]
            if g == 'X':
                print(Fore.BLUE + g, end=' ')  
            elif g == 'O':
                print(Fore.RED + g, end=' ')  
            else:
                print(Fore.WHITE + g, end=' ')  
        print(Fore.WHITE) 
    print()
    
def enter_rc(player):   
    while True:
        row = int(input('row: '))
        if 0 <= row <= 3:
            pass
        else:
            print('WARNING! Out of range, Try Again ...')
            continue 
        column = int(input('column: '))
        if 0 <= column <= 3:
            pass
        else:
            print('WARNING! Out of range, Try Again ...')
            continue
        
        if game[row - 1][column - 1] == '_':  
            if player == 1:
                game[row - 1][column - 1] = 'X'
            elif player == 2:
                game[row - 1][column - 1] = 'O'
            break
        else:
            print('WARNING! Repetitive selection, Try Again ...')
            
def enter():   
    while True:
        row = int(input('row: '))
        if 0 <= row <= 3:
            pass
        else:
            print('WARNING! Out of range, Try Again ...')
            continue 
        column = int(input('column: '))
        if 0 <= column <= 3:
            pass
        else:
            print('WARNING! Out of range, Try Again ...')
            continue
        
        if game[row - 1][column - 1] == '_':     
            game[row - 1][column - 1] = 'X'
            break
        else:
            print('WARNING! Repetitive selection, Try Again ...')

def enter_rc_computer():
    while True:
        r = random.randint(1, 3)
        c = random.randint(1, 3)
        
        if game[r - 1][c - 1] == '_':
            game[r - 1][c - 1] = 'O'
            break

def end_game():
    for i in range(3):
        if game[i][0] == 'X' and game[i][1] == 'X' and game[i][2] == 'X':
            return 1
        if game[i][0] == 'O' and game[i][1] == 'O' and game[i][2] == 'O':
            return 2 
        
    for i in range(3):
        if game[0][i] == 'X' and game[1][i] == 'X' and game[2][i] == 'X':
            return 1
        if game[0][i] == 'O' and game[1][i] == 'O' and game[2][i] == 'O':
            return 2 
    
    if game[0][0] == 'X' and game[1][1] == 'X' and game[2][2] == 'X':
        return 1
    if game[0][0] == 'O' and game[1][1] == 'O' and game[2][2] == 'O':
        return 2
        
    return 0
    
print('WELCOME \n mode 1: 1 player \n mode 2: 2 players')

while True:
    game = [['_', '_', '_'],
        ['_', '_', '_'],
        ['_', '_', '_']]
    
    m = int(input('mode: '))
    start_time = time.time()

    if m == 1:
        flag = 0        
        for i in range(9):
            if i % 2 == 0:
                enter()
            elif i % 2 != 0:
                enter_rc_computer()
        
            show_game()
            
            e = end_game()
            if e != 0:
                flag = 1
                print('End Game')
                if e == 1:
                    print('Player is Winner :)')
                if e == 2:
                    print('Computer is winner :(')
                break

        if flag == 0:
            print('End Game')
            print('DRAW :|')

    else:
        flag = 0        
        for i in range(9):
            if i % 2 == 0:
                enter_rc(1)
            elif i % 2 != 0:
                enter_rc(2)
            
            show_game()
            
            e = end_game()
            if e != 0:
                flag = 1
                print('End Game')
                if e == 1:
                    print('Player One WIN :)')
                if e == 2:
                    print('Player Two WIN :)')
                break

        if flag == 0:
            print('End Game')
            print('DRAW :|')
    
    print("--- time for this round of game = %s seconds ---" % (time.time() - start_time))        
    question = input('Play again (0) - Exit (else 0) \n')
    if question == '0':
        continue
    else:
        break