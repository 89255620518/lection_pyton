# def f(x):
#     return x * x
# a = f        # Переменная "а" - хранить ссылку на переменную "f"
# print(f(5))
'''
def math(op, x, y):
    print(op(x, y))

math(lambda a, b: a * b, 5, 45)
'''

# Задача №1
# В списке хранятся числа. Нужно выбрать только четные числа и составить
# список пар (число: квадрат числa)
'''
data = [1, 2, 3, 5, 8, 15, 23, 38]

res = list()

for i in data:
    if i % 2 == 0:
        res.append((i, i**2))
print(res)
'''
# С использованием функцию  "lambda"
'''
def select(f, col):
    return[f(x) for x in col]

def where(f, col):
    return [x for x in col if f(x)]

data = [1, 2, 3, 5, 8, 15, 23, 38]

res = select(int, data)
print(res)
res = where(lambda x: x % 2 == 0, res)
print(res)
res = list(select(lambda x: (x, x**2), res))
print(res)
'''

### ФУНКЦИЯ "map"
'''
list_1 = [x for x in range(1, 20)]
print(list_1)

list_1 = list(map(lambda x: x + 10, list_1))
print(list_1)
'''

# Задача:
# С клавиатуры вводится некий набор чисел, в качестве разделителя
# используется пробель. Этот набор чисел будет считан в качестве
# строки. Как превратить "list" строк в "list" чисел?

# .split(', ') - преобразует строку в список
'''
data = '15 156 96 3 5 8 52 5'  # -> строка
# print(data)
# data = data.split()            # -> преобразовали в список
# print(data)

data = list(map(int, data.split()))
print(data)
'''

### ФУНКЦИЯ "filter"
'''
data = [15, 65, 9, 36, 175]
res = list(filter(lambda x: x % 10 == 5, data))
print(res)
'''

'''
data = [1, 2, 3, 5, 8, 15, 23, 38]

res = map(int, data)
res = filter(lambda x: x % 2 == 0, res)
res = list(map(lambda x: (x, x**2), res))
print(res)
'''

### ФУНКЦИЯ "zip"

# zip ([1, 2, 3], ['o', 'д', 'т'], ['f', 's', 't']) -> [(1, 'o', 'f'), (2, 'д', 's'), (3, 'т', 't')]
'''
users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 14, 7]
data = list(zip(users, ids))
print(data)                  # [('user1', 4), ('user2', 5), ('user3', 9), ('user4', 14), ('user5', 7)]

# Функция "zip()" пробегает по минимальному входящему набору:

users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 14, 7]
salary = [111, 222, 333]
data = list(zip(users, ids, salary))
print(data)                  # [('user1', 4, 111), ('user2', 5, 222), ('user3', 9, 333)]
'''

### ФУНКЦИЯ "enumerate"
'''
# enumerate(['Казань', 'Смоленск', 'Рыбки', 'Чикаго']) -> [(0, 'Казань'), (1, 'Смоленск'), (2, 'Рыбки'), (3, 'Чикаго')]
# функция "enumerate" - позволяет пронумеровать набор данных

users = ['user1', 'user2', 'user3']
data = list(enumerate(users))
print(data)                  # [(0, 'user1'), (1, 'user2'), (2, 'user3')]
'''

### ФАЙЛЫ
"""
# Файлы в текстовом формате использует для:
# * Хранение данных
# * Передачи данных в клиент-серверных проектах
# * Хранение конфигов
# * Логирования действий

# Что нужно для работы с файлами
# 1. Завести переменную, которая будет связана с этим текстовым файлом
# 2. Указать путь к файлу
# 3. Указать, в каком режиме мы будем работать с файлом

# Варианты режима (мод):

# "а" - открытие для добавления данных
#     * Позволяет дописывать что-то в имеющийся файл.
#     * Если вы попробуете дописать что-то в несущ. файл, то файл
#       будет создан и в него начнется запись
# "r" - открытие для чтения данных.
#     * Позволяет читать данные из файла.
#     * Если вы попробуете считать данные из файла, которого не сущ., программа
#       выдаст ошибку.
# "w" - открытие для записи данных.
#     * Позволяет записывать данные и создавать файл, если его не сущ.

# Миксованные файлы
# "w+" * Позволяет открывать файл для записи и читать из него.
#      * Если файла не сущ., он будет создан

# "r+" * Позволяет открывать файл для чтения и дописывать в него.
#      * Если файл не сущ., программа выдаст ошибку.

# Открываем файл "file.txt" и закрываем "close"
'''
colors = ['red', '8899', 'blue']
data = open('file.txt', 'a')      # Здесь указываем режим, в котором будем работать
data.writelines(colors)           # разделителей не будет
data.close()
'''

# Удаляет старые данные и добавляем новые в созданном файле
''' 
with open('file.txt', 'w') as data:
    data.write('line 1\n')
    data.write('line 2\n')
'''

# Режим чтения
'''
path = 'file.txt'
data = open('file.txt', 'r')
for line in data:
    print(line)
data.close()
'''
"""

### МОДУЛЬ "os"
'''
# os.chdir(path) - Смена текущуй диретории
#     import os
#     os.chdir('C:\Users\Хасанов Эркин\OneDrive\Рабочий стол\Python')
# os.getcwd() - текущая рабочая директория
#     import os
#     print(os.getcwd())

# os.path - явл. вложенным модулем в модуль "os" и реализует некоторые полезные
#           функции для работы с путями, такие как:
#     * os.path.basename(path) - базовое имя пути
#        import os
#       print(os.path.basename('c:/Users/Хасанов Эркин/OneDrive/Рабочий стол/Python/Лекции/Лекция_4.py'))
       # 'Лекция_4.ру' - выведит имя файла
#     * os.path.abspath(path) - возвращает нормализованный абсолютный путь
#        import os
#        print(os.path.abspath('Лекция_4.py'))
       # 'C:\Users\Хасанов Эркин\OneDrive\Рабочий стол\Python\Лекция_4.py'
'''     

### МОДУЛЬ "shutil"
'''
# import shutil

# * shutil.copyfile(src,dst) - копирует содержимое (но не метаданные) файла "scr" в файл "dst"
# * shutil.copy(scr, dst) - копирует содержимое файла "scr" в файл или папку "dst"/
# * shutil.rmtree(path) - удаляет тек. директорию и все поддиректории: "path" должен указывать
#                         на директорию, а не символическую ссылку.
'''

