
from types import prepare_class


n = int(input('Enter your number: '))
paskal = [['-' for i in range(n)] for j in range(n)]

for i in range(n):
    for j in range(i + 1):
        if j == 0 or j == i:
            paskal[i][j] = 1
        else:
            paskal[i][j] = int(paskal[i - 1][j - 1]) + int(paskal[i - 1][j])

for i in range(n):
    for j in range(n):
        if paskal[i][j] != '-':
            print(paskal[i][j], end=' ')
    print()