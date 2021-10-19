import random
from colorama import Fore

print('You must choose between front or back in each round')

user = 0
pc1 = 0
pc2 = 0
game_list = ['front', 'back']

while (True):
    user_choice = input(Fore.CYAN + 'front or back: ')
    pc1_choice = random.choice(game_list)
    pc2_choice = random.choice(game_list)
    
    print(Fore.MAGENTA + 'u:', user_choice, 'p1:', pc1_choice, 'p2:', pc2_choice)
    
    if (user_choice == pc1_choice and pc1_choice == pc2_choice):
        continue
    elif (user_choice == pc1_choice and pc1_choice != pc2_choice):
        pc2 += 1
    elif (user_choice == pc2_choice and pc1_choice != pc2_choice):
        pc1 += 1
    elif (user_choice != pc1_choice and pc1_choice == pc2_choice):
        user += 1
    else:
        print('error')
        
    if (user == 5):
        print(Fore.WHITE + 'Winner = USER')
        break
    if (pc1 == 5):
        print(Fore.WHITE + 'Winner = Computer1')
        break
    if (pc2 == 5):
        print(Fore.WHITE + 'Winner = Computer2')
        break