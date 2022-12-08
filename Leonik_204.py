# Дан список. Выведите те его элементы, которые встречаются в списке только один раз.
# Элементы нужно выводить в том порядке, в котором они встречаются в списке.
stroka= input ("введите строку через пробел:")
raz= stroka.split(' ')

oops=[]
for s in raz:
    if s  not in oops:
        oops.append(s)
    else: oops.remove(s)
print('Элементы встречающиеся один раз:', oops)

#2.Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
# Например, два одинаковых элемента образуют одну пару, 3 элемента образуют 3 пары, 4 элемента образуют 6 пар и т.д.
# Воспользуйтесь формулой: Количество пар = (Общее число одинаковых элементов X (Общее число одинаковых элементов) — 1) / 2
spsk= [1, 2, 35, 55, 876, 454, 44, 58, 55, 55, 478, 1, 2, 35, 44]
count=0
# spsk2=set(spsk)
# print(spsk2)
for i in range(len(spsk)):
    for j in range(i+1,len(spsk)):
        if spsk[i]==spsk[j]:
            count+=1
print(count)


#    3. Даны два кортежа:
# Необходимо определить:
#  1) Сумма элементов какого из кортежей больше и вывести соответствующее сообщение на экран (Сумма больше в кортеже - ..)
# 2) Вывести на экран порядковые номера минимальных и максимальных элементов этих кортежей (index).
C_1 = (35, 78,21,37, 2,98, 6, 100, 231)
C_2 = (45, 21,124,76,5,23,91,234)
sum_c_1= (sum(C_1))
sum_c_2=(sum(C_2))
if sum(C_1)> sum(C_2):
    print ('Сумма больше в кортеже - С_1')
elif sum(C_1)==sum(C_2):
    print('кортежи равны')
else: print('Сумма больше в кортеже - С_2')
print('Порядковые номера максимальных значений :', C_1.index(max(C_1)), C_2.index(max(C_2)) )
print('Порядковые номера минимальных значений :', C_1.index(min(C_1)), C_2.index(min(C_2)) )


#4. Создайте словарь из строки ' An apple a day keeps the doctor away' следующим образом:
# в качестве ключей возьмите символы строки, а значениями пусть будут числа,
# соответствующие количеству вхождений данной буквы в строку.
# Заглавные буквы нужно считать строчными. Пробелы не учитывать.
apple= 'An apple a day keeps the doctor away'.lower()
apple=apple.replace(' ','')
print(apple)
counter=[]
list_apple=[]

for letter in apple:
    if letter not in list_apple:
        list_apple.append(letter)
        counter.append(apple.count(letter))
print(counter)
print(list_apple)
di_apple= dict(zip(list_apple, counter))
print(di_apple)


#5. Даны два списка чисел. Посчитайте, сколько чисел содержится одновременно как в первом списке, так и во втором.
z=[45,95,48,75,24,55,47]
x=[1,2,35,45,55,8,72]
print('Количество чисел:',len(set(z)&set(x)))

#6.В текстовый файл построчно записаны фамилия и имя учащихся класса и его оценка за контрольную.
# Вывести на экран всех учащихся, чья оценка меньше 3 баллов и посчитать средний балл по классу

srednee=0
lohi=[]
students= open('strudents.txt', 'r' ,encoding='utf-8')
stu=students.read()
studentslist= stu.split('\n')
print(studentslist)
for st in studentslist:
    srednee+=int(st[-1])
    if int(st[-1])<3:
        lohi.append(st)
print('Учащиеся,чья оценка меньше 3: ', lohi)
print('средний балл класса:', srednee/len(studentslist))
students.close()


#     7. В файле input.txt через пробел записаны два числа (int или float, можно отрицательные).
# В файл output.txt вывести результат вычетания (первое число минус второе).

npt= open('input.txt','r')
lk=(npt.read().split(' '))
print(lk)
rlk=int(lk[0])-int(lk[1])

with open('output.txt', 'w') as tpt:
     tpt.write(f'{rlk}')
npt.close()




print('Привет, как дела?')



