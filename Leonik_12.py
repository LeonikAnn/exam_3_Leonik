def addition(x,y):
    return x+y
def subtruction(x,y):
    return x-y
def multiplication(x,y):
    return x*y
def division(x,y):
    return x/y
while True:
    number1= float(input ('Введите первое число:'))
    number2 = float(input('Введите второе число:'))
    sigh= input('Введите знак: +,-,*,/')
    if sigh== '+': print (addition(number1,number2))
    elif sigh == '-': print(subtruction(number1, number2))
    elif sigh == '*': print(multiplication(number1, number2))
    try:
        if sigh == '/': print(division(number1, number2))

    except ZeroDivisionError:
        if number2 == 0: print('деление на ноль!!')
    next= input('Для выхода введите  "0"')
    if next== '0':
        break
    else: continue

