def table(n, m):
    for i in range(1, n+1):
        p = ''
        for j in range(1, m+1):
            x = j * i
            p += str(x) + ' '
        print(p)            

n = int(input('n: '))
m = int(input('m: '))

table(n, m)
