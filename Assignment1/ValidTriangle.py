
a = float(input('a is '))
b = float(input('b is '))
c = float(input('c is '))

if (a < (b + c) and b < (a + c) and c < (a + b)):
    print('Valid :)')
else:
    print('Not Valid :(')