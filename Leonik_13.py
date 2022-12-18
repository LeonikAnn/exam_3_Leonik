def decorator(func):
    def wrapper(argument):
        print(f'Тип данных:{type(argument)}')
        func(argument)
    return wrapper


k = (487, 'hello', 5, 'school', 'fog', 148, 55)
sp = ['school', 455, 'lessons', 5, 88, 'computer']
stroka= 'У Лукоморья дуб зеленый, золотая цепь на дубе том'
numberfd = 12356789
@decorator
def fun(d):
    if type(d)== tuple:
        for l in d:
            if l ==str(l):
                print(f'количество букв в строке {l}: {len(l)} ')
    elif type(d) == list:
        counter_dig= 0
        counter_letter = 0
        d = ' '.join(map(str,d))
        for lst in d:
            if lst.isdigit(): counter_dig += 1
            if lst.isalpha(): counter_letter += 1

        print(f'Количество букв: {counter_letter}, Количество цифр: {counter_dig}')
    elif type(d) == str:
        count_let = 0
        print('количество букв в строке:', len([i for i in d if i.isalpha()]))
    elif type(d) == int:
        count = 0
        while d > 0:
            odd = d%10
            if odd%2 !=0: count+=1
            d= d//10
        print(f'Количество нечетных цифр в числе: {count}')

fun(k)
fun(sp)
fun(stroka)
fun(numberfd)

