first_number = int(input('First number is '))
second_number = int(input('Second number is '))

for i in range(1, min(first_number, second_number)+1):
    if (first_number % i == 0 and second_number % i == 0):
        answer = i
        
print(answer)

