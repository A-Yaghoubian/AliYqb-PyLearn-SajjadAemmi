
seconds = int(input('All seconds is '))

h = seconds // 3600
seconds %= 3600

m = seconds // 60
seconds %= 60

s = seconds

if (h < 10):
    h = '0' + str(h)

if (m < 10):
    m = '0' + str(m)

if (s < 10):
    s = '0' + str(s)

s = str(s)
m = str(m)
h = str(h)
        
print(h + ':' + m + ':' + s)