
fullName = input('Enter Your Full Name: ')


math = float(input('Enter Mathematical point: '))
physics = float(input('Enter Physics point: '))
chemistry = float(input('Enter Chemistry point: '))
mean = (math + physics + chemistry) / 3

if (mean >= 17):
    print(fullName, 'is Great')

if (mean < 17 and mean >= 12):
    print(fullName, 'is Normal')

if (mean < 12):
    print(fullName, 'is Fail')