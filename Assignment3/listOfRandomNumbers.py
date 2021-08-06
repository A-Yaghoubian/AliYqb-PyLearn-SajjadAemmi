import random

while True:
    n = int(input('Your n is: '))

    if (n > 200 or n < 0):
        print('WARNING!, n must between 0 - 200, Please enter n again')
    else:
        break

numbers = random.sample(range(0, 200), n)
print(numbers)