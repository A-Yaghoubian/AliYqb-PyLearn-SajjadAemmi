# STR = input()
# print(len(STR.split()))
# -------------------------------

def counter(string):
    x = 0
    for i in range(len(string)):
        if ((string[i] != ' ' and i == 0) or (string[i] != ' ' and string[i-1] == ' ')):
            x += 1
    
    return x

STR = input('Please enter your sentence ==> ')
count = counter(STR)
print(count)
