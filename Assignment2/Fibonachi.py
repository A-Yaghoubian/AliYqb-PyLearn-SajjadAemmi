
n = int(input('Please enter yout number.   n = '))

Fib_list = []

for i in range(n):
    if (i == 0 or i == 1):
        Fib_list.append(1)
    
    else:
        Fib_list.append(Fib_list[i-1]+Fib_list[i-2])

Fib_list = list(map(str, Fib_list))        
output = ', '.join(Fib_list)
print(output)
 