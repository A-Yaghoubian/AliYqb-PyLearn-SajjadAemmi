def board(n, m):
    for i in range(n):
        p = ''
        for j in range(m):
            if (i % 2 == 0):
                if (j % 2 == 0):
                    p += '#'
                else:
                    p += '*'
            else:
                if (j % 2 == 0):
                    p += '*'
                else:
                    p += '#'
        print(p)            

n = int(input('n: '))
m = int(input('m: '))

board(n, m)
