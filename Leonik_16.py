#ДЗ на четверг:
# Класс Company:

# Создайте класс Company
class Company:
# Создайте статическое свойство levels, которое будет содержать
# (как словарь) все уровни квалификации программиста: 1:junior, 2:middle, 3:senior, 4:lead.
    levels= {1:'junior', 2:'middle', 3:'senior', 4:'lead'}
    def __init__(self, index):

        self._index = index
        self._levels =Company.levels[self._index]
        print(self._index, self._levels)


# Создайте метод __init__(), внутри которого будут определены два protected свойства:
# 1) _index - передается параметром и 2) _levels - принимает из словаря levels значение с ключом _index

# Создайте метод _level_up(), который будет переводить программиста на следующий уровень
    def _level_up(self):
        if self._index < 4:
            self._index +=1
            self._levels = Company.levels[self._index]
            print (f'Вы достигли уровня:{self._index} - {self._levels}')
        elif self._index == 4:
            print('Достигнута максимальная квалификация')




# Создайте метод is_lead(), который будет проверять, что программист достиг последней квалификации
    def is_lead(self):
        if self._index == 4:
            print ('Последняя квалификация достигнута')
        else: print(f'Ваша квалификация: {self._index}')

codehead = Company(3)
codehead._level_up()
codehead.is_lead()


# Класс Programmer:
class Programmer(Company):
# Создайте метод __init__(), внутри которого будут определены 3 динамических свойства:
#1) name - передается параметром, является публичным, 2)age - возраст 3) level – уровень квалификации на основе словаря из Company
    def __init__(self, name, age):
        super().__init__(int(input('Введите ваш уровень:')))
        self. name = name
        self.age = age
        self.level = self.levels
# Создайте метод work(), который заставляет программиста работать, что позволяет ему становиться более квалифицированным
# с помощью метода _level_up() родительского класса
    def work(self):
        print('Working...')
        return self._level_up()

# Создайте мeтод info(), который выведет информацию о вас: имя, возраст, квалификацию
    def info(self):
        print(f'Имя:{self.name}\nВозраст: {self.age}\nКвалификация:{self.level[self._index]}')

# Создайте статический метод knowledge_base(), который выведет в консоль справку по программированию (просто любой текст).
    @staticmethod
    def knowledge_base():
        print('''Объектно-ориентированное программирование — это парадигма программирования,\nкоторая позволяет структурировать программы таким образом, что свойства и поведение объединяются в отдельные объекты.\nКлассы используются для создания определяемых пользователем структур данных. Кроме того, классы определяют функции,\nназываемые методами, которые определяют поведение и действия, которые объект, созданный на основе класса, может выполнять с его данными.''')

Anya = Programmer('Anya', 26)
Anya.work()
Anya.info()
Programmer.knowledge_base()