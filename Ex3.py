
weight = int(input('Enter Weight in kg: '))
height = float(input('Enter Height in cm: '))

BMI = weight / (height/100)**2

if BMI < 18.5:
    print('Under Wight')

if BMI > 18.5 and BMI < 24.9 :
    print('Normal')

if BMI > 25 and BMI < 29.9 :
    print('Over Wight')

if BMI > 30 and BMI < 34.9 :
    print('OBESE')

if BMI > 35 :
    print('Extremely OBESE')



