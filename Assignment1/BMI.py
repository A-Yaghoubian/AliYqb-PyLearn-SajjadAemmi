w = float(input('Enter your Weight (in kg): '))
h = float(input('Enter your Height (in m): '))

BMI = w / (h ** 2)
BMI = round(BMI, ndigits=1)

if (BMI < 18.5):
    print('your BMI is:', BMI, ' and you are UNDERWEIGHT')
elif (BMI >= 18.5 and BMI <= 24.9):
    print('your BMI is:', BMI, ' and you are NORMAL')
elif (BMI >= 25 and BMI <= 29.9):
    print('your BMI is:', BMI, ' and you are OVERWEIGHT')
elif (BMI >= 30 and BMI <= 34.9):
    print('your BMI is:', BMI, ' and you are OBESE')
else:
    print('your BMI is:', BMI, ' and you are EXTREMELY OBESE')
