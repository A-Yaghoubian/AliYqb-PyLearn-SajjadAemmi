import random

options = ['rock', 'paper', 'scissors']
scores = {'user':0, 'computer':0}

def true_choice(ch):
    if ch == 'rock' or ch == 'paper' or ch == 'scissors':
        return True
    else:
        return False
    
def game(user, pc):
    if user == pc:
        print('Draw\tcomputer choice : ', pc)
    
    elif (user == 'rock' and pc == 'scissors') or (user == 'paper' and pc == 'rock') or (user == 'scissors' and pc == 'paper'):
        scores['user'] += 1
        print('Win\tcomputer choice : ', pc)
    
    else:
        scores['computer'] += 1
        print('Lose\tcomputer choice : ', pc)

def finish(m):
    if scores['user'] == m:
        print('YOU ARE WINNER :)')
        return True
    elif scores['computer'] == m:
        print('COMPUTER IS WINNER :(')
        return True
    else:
        return False

while True:    
    scores['user'] = 0
    scores['computer'] = 0
    mode = int(input('Enter your game mode (1 or 3 or 5) : '))

    if (mode == 1 or mode == 3 or mode == 5):
        while True:
            computer_choice = random.choice(options)
            while True:    
                user_choice = input('Your choice = ')
                if true_choice(user_choice):
                    break
            
            game(user_choice, computer_choice)
            f = finish(mode)
            if f == True:
                break
        ex = input('EXIT ? (y or n) ')
        if ex == 'y':
            print('See you soon ...')
            break
            
    else:
        continue