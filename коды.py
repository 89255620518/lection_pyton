# Cоздать список, состоящий из четных чисел 
'''
# 1) в диапазоне от 1 до 100
list_1 = []
for i in range(1, 101):
    list_1.append(i)
print(list_1)
# Запишем решение сокращенно
list_1 = [i for i in range(1, 101)]
print(list_1)

# 2) только четные числа
list_1 = [i for i in range(1, 101) if i % 2 == 0]
print(list_1)

# Cоздать пару каждому из чисел (кортежи)
list_1 = [(i, i) for i in range(1, 101) if i % 2 == 0]
print(list_1)

# Умножить на 2
list_1 = [i * 2 for i in range(10) if i % 2 = 0]
print(list_1)
'''

# Округление в большую сторону
'''
import math
dayDistance = int(input('Введите расстояние за день: '))
overallDistance = int(input('Введите общее расстояние: '))
print(f"{math.ceil(overallDistance / dayDistance)} ")
'''

'''
class_1 = 3
m = class_1//2 + class_1%2
print(m)                       # 2
'''

# Сумма трехзначного числа:
'''
n1 = n // 100 # Нахождение первой цифры числа
n2 = (n % 100) // 10 # Нахождение второй цифры числа
n3 = n % 10 # Нахождение третьей цифры числа
res = n1 + n2 + n3
'''

# Нахождение каждой цифры числа
'''
n = 123456
n1 = n // 100000            # 1
n2 = (n % 100000) // 10000  # 2
n3 = (n % 10000) // 1000    # 3
n4 = (n % 1000) // 100      # 4
n5 = (n % 100) // 10        # 5
n6 = n % 10                 # 6
'''

# Нахождение минимума и максимума
'''
import random

num_N = int(input('Введите кол-во арбузов: '))
watermelon = []

for i in range(num_N):
    watermelon.append(random.randint(1, 10))
print(watermelon)

print(min(watermelon), max(watermelon))
'''

# Нахождения факториала от 1 до N
'''
num_n = int(input('Введите число: '))
factorial_N = 1

while num_n > 0:
    factorial_N = factorial_N * num_n
    num_n -= 1
print(factorial_N)
'''

# Cдвиг налево и направо
"""
## через срезы
'''
k = int(input('Введите число К: '))
num_list = num_list[-k:] + num_list[:-k] # cдвиг справо
num_list = num_list[k:] + num_list[:k]   # сдвиг налево
'''
##через ".pop"
'''
for _ in range(k):
    num_list.insert(0, num_list.pop())
'''
"""


# Убирает пробелы .strip
'''
.strip(" ")
'''

# Найдите количество и выведите его.
'''
list_1 = [1, 2, 3, 4, 5]
k = 3

print(list_1.count(k))
'''

# Переводим все буквы на верхний регистр
'''
points_en = {1: 'AEIOULNSTR', 2: 'DG', 3: 'BCMP', 4: 'FHVWY', 5: 'K', 8: 'JX', 10: 'QZ'}
points_ru = {1: 'АВЕИНОРСТ', 2: 'ДКЛМПУ', 3: 'БГЁЬЯ', 4: 'ЙЫ', 5: 'ЖЗХЦЧ', 8: 'ШЭЮ', 10: 'ФЩЪ'}
word = k.upper()  # переводим все буквы в верхний регистр
'''

# Сумма всех элементов с помощью функции
'''
def summa(spisok):
    s = 0
    for item in spisok:
        s += item
    print(s)

summa([5, 8, 13, 12])
'''

# input: a a a b c a a d c d d
# output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
'''
spisok_list = 'a a a b c a a d c d d'
list_1 = spisok_list.split(' ')   # - получился лист
d = {}
final_str = ''
for i in list_1:   # Выделили уникальные элементы "a b c d"
    if i in d:
        d[i] += 1  # если есть довавляем +1
        final_str += f'{i}_{d[i]} '
    else:
        d[i] = 0   # если нет, то пропускаем
        final_str += f'{i}'
print(final_str)
'''

# Заменили точки на пробелы 
'''
text = text.replace('.',' ').split()
'''
# почистили от всех знаков
'''
i.strip('.,?!\n').lower()
'''

# Cумма всех значений от 1 до N
'''
def sum_numbers(n):
    summa = 0
    for i in range(1, n+1):
        summa += i
    return summa

print(sum_numbers(5))
'''

# Импортируем функцию
'''
from lec_3 import max1
print(max1(5, 9))
'''
# Импортируем функцию, как "m1"
'''
import lec_3 as m1
print(m1.max1(9,6))
'''

# Последовательности Фибоначчи
'''
def fib_num (n):
    if n in [1, 2]:
        return 1
    return fib_num(n-1) + fib_num(n-2)

list_1 = []

for i in range(1, 10):
    list_1.append(fib_num(i))
print(list_1)
'''

# Быстрая сортировка(разделяй и властвуй)
'''
def qwick_sort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]
    return qwick_sort(less) + [pivot] + qwick_sort(greater)

print(qwick_sort([10, 5, 2, 4]))
'''

# Сортировка слияния
'''
def merge_sort (nums):
    if len(nums) > 1:
        mid = len(nums) // 2   # Середина
        left = nums[:mid]      # левая сторона
        right = nums[mid:]     # Правая сторона
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1                 # При каждой операции, добавлялся новое значение
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1

list_1 = [2,3,4,5,6,7,8,9,32, 12,]

merge_sort(list_1)
print(list_1)
'''

# Напишите функцию f, которая на вход принимает два числа a и b, 
# и возводит число a в целую степень b с помощью рекурсии.
'''
a = int(input('Введите число a \n'))
b = int(input('Введите числ b \n'))

def f(a, b):
  if b == 0:
    return 1
  return f(a, b - 1) * a

print(f(a, b))
'''

# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых 
# неотрицательных чисел. Из всех арифметических операций допускаются 
# только +1 и -1. Также нельзя использовать циклы.
'''
def sum(a, b):
    a += b
    return a

a = 3
b = 5
print(sum(a, b))
'''

# [18, [[20, [10, 7]], 15]] - cумма всех элементов
'''
def sum_count(sp):
    total = 0     # переменная для суммы
    for item in sp:
        #if type(item) == type([]):
        if isinstance(item,list):
            total = total + sum_count(item)
        else:
            total += item
    return total
'''

# Треб. вывести те элементы первого массива (в том порядке
# в каком они идут в первом массиве), которых нет во втором массиве.
'''
n = [randint(1,10) for _ in range(5)]
m = [randint(1,7) for i in range(5)]
print(n,m)
res = [x for x in n if x not in m]
print(res)
'''

# Подсчитайте, сколько в нем пар элементов,
# равных друг другу
'''
list_1 = [randint(1,10) for i in range(6)]
pair_count = sum(list_1.count(i)//2 for i in set(list_1))
print(list_1)
print(pair_count)
'''

# SQLite создание базы данных
'''
import sqlite3 as sl

# Подключаемся к базы данных
con = sl.connect("gb.db")   # устанавливаем соединения с базой данных
cur = con.cursor()          # если не было, то создастся

# создаем таблицу с помощь "Create table"
cur.execute("""CREATE TABLE IF NOT EXISTS user (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER
)""")
# CREATE TABLE IF NOT EXISTS user - если нету файла то создаст, если есть то не даст ошибку и пропустить
# id INTEGER PRIMARY KEY AUTOINCREMEN - автоматический добавляет нумерацию
con.commit()
# cur.execute("INSERT INTO user (name,age) VALUES ('Петров', 33)") # Добавляем данные
# con.commit() 
cur.execute("select * from user")
# print(cur.fetchall())

for row in cur.fetchall():
    print(row)
'''

# Cоздать файл "json"
'''
phonebook = {'Дядя Петя': {'phone_numbers': ["12321123", "123123"], 'birthday': '01.03.2021', 'e-mail': 'petya@mail.ru'}}

with open("phonebook.json", 'w', encoding= 'utf-8' ) as phone_bookjson:
    phone_bookjson.write(json.dumps(phonebook, ensure_ascii= False))
'''