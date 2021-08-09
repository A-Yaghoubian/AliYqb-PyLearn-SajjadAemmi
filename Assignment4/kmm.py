first_number = int(input('First number is '))
second_number = int(input('Second number is '))
ma = max(first_number, second_number)
mi = min(first_number, second_number)

for i in range(1, (ma * mi)):
    if ((ma * i) % mi == 0):
        answer = (ma * i)
        break
        
print(answer)