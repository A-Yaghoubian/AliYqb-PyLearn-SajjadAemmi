import random
from typing import Text

words = ['ali', 'moeen', 'amirali', 'rajab', 'amin', 'jafar', 'rasool', 'omidreza', 'saeideh', 'mahsa', 'fatemeh', 'najaf', 'danesh', 'alireza', 'aidin', 'maryam', 'masoumeh', 'reza', 'sajjad', 'benyamin', 'shadi', 'rezvaneh', 'negin', 'seyedali', 'amirhosein', 'hananeh', 'mahshid', 'mahdis', 'parvaneh', 'parisa', 'azar', 'nahid', 'nahich', 'mahyar', 'arash', 'korosh', 'mohammadhadi', 'arman', 'ghazal', 'elham']

n = int(input('Levels ? (0:Easy, 1:Normal , 2:Hard)'))
if (n == 0):
    joon = 15
elif (n == 1):
    joon = 10
elif (n == 2):
    joon = 5
    
word = random.choice(words)
p = []
for i in range(len(word)):
    p.append('_')

while joon > 0:
    print(' '.join(p))
        
    if ((''.join(p)) == word):
        print('You Win *-*')
        break
    
    user_character = input()
    user_character = user_character.lower()
    
    if (user_character in word):
        print('Yes  Joon = ', joon)
        for i in range(len(word)):
            if (word[i] == user_character):
                p[i] = user_character        
                
    else:
        joon -= 1
        print('No  Joon = ', joon)
