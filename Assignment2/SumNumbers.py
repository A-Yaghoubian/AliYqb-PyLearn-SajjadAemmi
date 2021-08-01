
sum = 0

while True:
    n = input('Please Enter Your Number ==> ')
    if (n == 'exit'):
        break
    else:
        n = int(n)    
        sum += n
        
print('Sum Numbers:', sum)