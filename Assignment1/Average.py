first_name = input('Fisrt name: ')
last_name = input('Last name: ')

while True:
    score1 = float(input('score1: '))
    if (score1 > 20 or score1 < 0):
        print('WRONG! scroe is between 0 - 20')
        continue
    
    score2 = float(input('score2: '))
    if (score2 > 20 or score2 < 0):
        print('WRONG! scroe is between 0 - 20')
        continue
    
    score3 = float(input('score3: '))
    if (score3 > 20 or score3 < 0):
        print('WRONG! scroe is between 0 - 20')
        continue
    
    break

avg = (score1 + score2 + score3) / 3

if (avg < 12):
    print('Your average:', avg, 'FAIL !')
    
elif (avg >= 12 and avg < 17):
    print('Your average:', avg, 'Normal ...')
    
else:
    print('Your average:', avg, 'Great :)')