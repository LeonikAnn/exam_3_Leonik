# Класс состоит из двух методов
# 1 метод: принимает либо строку, либо число.
# Если передаю строку: если произведение количества гласных и согласных
# меньше или равно длине строки, то вывести все гласные. Иначе все согласные
# Если передаю число: вывести произведение суммы четных цифр на длину числа
# Использовать len в 1 методе нельзя, вместо len используйте второй метод.
# 2 метод: возвращает длину строки или числа. Можно использовать len
a1 = 'Привет, мир'
a2 = 45882543
class d_l:
    def __init__(self, a):
        self.a = a

    def func_2(self,a):
        return len(str(a))

    def prov(self, a):
        if type(a) == str:
            count_v = 0
            list_vowels = ''
            list_consonants = ''
            count_c = 0
            for i in a.lower():
                if i in 'aoeiuаоеуюыяёи':
                    count_v += 1
                    list_vowels += i
                elif i.isalpha():
                    count_c += 1
                    list_consonants += i
            if count_v*count_c <= self.func_2(a): return list_vowels
            else: return list_consonants
        if type(a) == int:
            a = str(a)
            sum_even = 0

            for j in a:
                if int(j)%2 == 0: sum_even += int(j)

            return sum_even* self.func_2(a)

stroka = d_l('123')
print(stroka.func_2(a1))
print(stroka.prov(a1))
print(stroka.func_2(a2))
print(stroka.prov(a2))





