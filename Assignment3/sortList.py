l = int(input('Input your length of list : '))
numbers = []
test = []

for i in range(l):
    print('(', i, ')')
    n = int(input('Enter your number: '))
    numbers.append(n)
    test.append(n)
    
test.sort()

if(numbers == test):
    print('Sorted :)')
else:
    print('Not sorted :(')