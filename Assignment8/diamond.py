n = int(input('Enter number of rows : '))

for i in range(1, n + 1):
    star = 2 * i - 1
    space = ((2 * n - 1) - star) // 2
    print(space * ' ',star * '*',space * ' ')
    
for i in range(n - 1, 0, -1):
    star = 2 * i - 1
    space = ((2 * n - 1) - star) // 2
    print(space * ' ',star * '*',space * ' ')