l = int(input('N = '))

draw = ''

for i in range(l):
    if (i % 2 == 0):
        draw += '*'
    else:
        draw += '#'
        
print(draw)