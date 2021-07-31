import math

while True:
    flag = 0
    
    first_number = float(input('Enter first number: '))
    print('operators: + - * / %(mod) **(power) sin cos tan cot radical factorial')
    operator = input('Enter your operator: ')
    if (operator == '+' or operator == '-' or operator == '*' or operator == '/' or operator == '%' or operator == '**'):    
        second_number = float(input('Enter second number: '))


    if (operator == '+'):
        answer = first_number + second_number
        
    if (operator == '-'):
        answer = first_number - second_number
        
    if (operator == '*'):
        answer = first_number * second_number
        
    if (operator == '/'):
        if (second_number != 0):
            answer = first_number / second_number
        else:          
            flag = 1
               
    if (operator == '%'): # mod
        answer = first_number % second_number
        
    if (operator == '**'): # power
        answer = first_number ** second_number

    if (operator == 'sin'):
        answer = math.sin(math.radians(first_number))
        
    if (operator == 'cos'):
        answer = math.cos(math.radians(first_number))
        
    if (operator == 'tan'):
        answer = math.tan(math.radians(first_number))
        
    if (operator == 'cot'):
        answer = math.cos(math.radians(first_number)) / math.sin(math.radians(first_number))
        
    if (operator == 'radical'):
        answer = math.sqrt(first_number)
        
    if (operator == 'factorial'):
        answer = math.factorial(first_number)
    
    if (flag == 0):    
        print(answer)
    else:
        print('Can not divide by zero(0)!')
        
    q = input('Do you want to do it again? (y/n)')

    if (q == 'n'):
        break 