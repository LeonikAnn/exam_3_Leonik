#Написать функцию, которая просит ввести имя и выводит на экран "Привет и введённое имя".
#Далее написать к функции декоратор, который изменяет функцию и переводит имя в заглавные буквы.
def upper_name(l):
     def wrapper(arg):
         print(f'Привет,{(arg.upper())}')
     return wrapper
@upper_name
def name(n):
    print(f'Привет,{n}')
name(input('Введите ваше имя:'))

#Найти сумму цифр числа с помощью рекурсии. 112 = 4
def sum(n):
    summa = 0
    while n > 0:
        summa += n%10
        n = n//10
    return summa

print('Cумма цифр числа:', sum(int(input('Введите число:'))))

