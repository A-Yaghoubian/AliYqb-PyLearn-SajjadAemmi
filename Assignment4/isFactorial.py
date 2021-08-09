def isFactorial(num):
    o = 1
    i = 1
    flag = 0
    while o <= num:
        if (o == num):
            print('yes')
            flag = 1
            break
        else:
            i += 1
            o *= i
            continue
    if flag == 0:
        print("no")    
    
number = int(input('Your number is '))
isFactorial(number)