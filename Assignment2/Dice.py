import random

while True:
    while True:
        x = input('type d for play DICE   ')
        
        if (x == 'd'):
            dice = random.randint(1, 6)
            if (dice == 6) :
                print(dice)
                print('WOowW 0_o It is very good, you can play again *-* ')
                continue        
                
            else:
                print(dice)
                break
            
        else:
            continue

    y = input('This round is finished, Do you want to play again? (y/n) ')
    if (y == 'y'):
        continue
    else:
        break