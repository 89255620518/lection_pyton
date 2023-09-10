### CПИСКИ
"""
'''
list_1 = []         # -> Создание пустого списка
list_1 = list()     # -> Создание пустого списка
list_1 = [7, 9, 11, 13, 15, 17]
print(list_1[0])    # -> 7
print(*list_1)      # Убираем скобки: 7 9 11 13 15 17
print(len(list_1))  # -> 6, размер нашего списка

for i in list_1:
    print(i)
'''

# Добавляем элемент в список
'''
list_1 = [1, 5]
print(list_1)        # -> [1, 5]

list_1.append(8)     # Добавляем элемент
print(list_1)        # -> [1, 5, 8]
'''
'''
list_1 = []          # []
print(list_1)        # [0]
for i in range(5):   # [0, 1]
    list_1.append(i) # [0, 1, 2]
    print(list_1)    # [0, 1, 2, 3]
                     # [0, 1, 2, 3, 4]
'''

# Удаление последнего элемента списка:
'''
list_1 = [12, 7, -1, 21, 0]
print(list_1.pop())       # -> удаляем посл элемент: 0
print(list_1)             # -> [12, 7, -1, 21]
print(list_1.pop())       # -> 21
print(list_1)             # -> [12, 7, -1]
'''

# Удаление конкретного элемента из списка:
'''
list_1 = [12, 7, -1, 21, 0]
print(list_1.pop(0))   # -> 12
print(list_1)          # -> [7, -1, 21, 0]
'''

# Добавление элемента на нужную позицию
'''
list_1 = [12, 7, -1, 21, 0]
print(list_1.insert(2, 11))  # -> (2, 11)  Добавляем на позицию 2ого элемента, знач 11
print(list_1)                # -> [12, 7, 11, -1, 21, 0]
'''

# Работа в списках
'''
list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(list_1[0])                # 1
print(list_1[1])                # 2
print(list_1[len(list_1)-1])    # 10
print(list_1[-5])               # 6
print(list_1[:])                # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list_1[:2])               # [1, 2]
print(list_1[len(list_1)-2:])   # [9, 10]
print(list_1[2:9])              # [3, 4, 5, 6, 7, 8, 9]
print(list_1[6:-18])            # []
print(list_1[0:len(list_1):6])  # [1, 7]
print(list_1[::6])              # [1, 7]
'''
"""

### КОРТЕЖИ
#tuple = t - это кортеж
"""
'''
t = ()         # Cоздание пустого кортежа
print(type(t)) # тип класса кортеж

t = (1)
print(type(t)) # тип класса целое число -> int
# Чтобы переобразовать в кортеж, нужно в конце поставить ","
t = (1, )
print(type(t)) # тип класса кортеж
'''

# Преобразование список в кортеж
'''
v = [1, 8, 9]
print(v)          # [1, 8, 9]
print(type(v))    # тип класса список
v = tuple(v)
print(v)          # (1, 8, 9)
print(type(v))    # тип класса кортеж
'''
# Кортеж разъединяем на переменные
'''
v = tuple(v)
print(v)          # (1, 8, 9)
print(type(v))
#разъединяем на переменные
a, b, c = v
print(a, b, c)    # 1 8 9
'''

t = (1, 2, 3, 5,)
print(t[1])
'''
for i in t:
    print(i)
#или
for i in range(len(t)):
    print(t[i])
'''
# Кортеж - это самый, что список, но мы кортеж не может изменять
"""

### СЛОВАРИ
"""
'''
dictionary = {}
dictionary = dict()
dictionary = {'left': '←', 'up': '↑', 'right': '→', 'down': '↓'}
print(dictionary)             # {'left': '←', 'up': '↑', 'right': '→', 'down': '↓'}
print(dictionary['left'])     # ←
print(dictionary['up'])       # ↑
# Меняем значение
dictionary['left'] = '↞'
print(dictionary['left'])     # ↞
#print(dictionary['type'])     # KeyError: 'type'
# Удаление элемента
del dictionary['up']          # 'up': '↑' - удаляем
print(dictionary)             # {'left': '↞', 'right': '→', 'down': '↓'}
# Добавляем элемент
dictionary[895] = 989898      # 895: 989898
print(dictionary)             # {'left': '↞', 'right': '→', 'down': '↓', 895: 989898}
print(dictionary.items())     # dict_items([('left', '↞'), ('right', '→'), ('down', '↓'), (895, 989898)])
'''

# Цикл "for" взаимодействует со словарем:
'''
for item in dictionary:     
    print('{}: {}'.format(item, dictionary[item]))    # left: ↞
                                                      # right: →
                                                      # down: ↓
    # Выводим ключ
    print(item)              # left
                              # right
                              # down
    # Выводим значение
    print(dictionary[item])   # ↞
                              # →
                              # ↓
'''
# или
'''
for (k, v) in dictionary.items():
    print(k, v)                 # left ↞
                                # right →
                                # down ↓
    # Выводим ключ                            
    print(k)                    # left
                                # right
                                # down
    # выводим значение
    print(v)                    # ↞
                                # →
                                # ↓
'''

'''
d = {}

d['q'] = 'qwerty'
print(d)           # {'q': 'qwerty'}

d['w'] = 'werty'
print(d)           # {'q': 'qwerty', 'w': 'werty'}
'''
"""

### МНОЖЕСТВО
# Множества содержат в себе уникальные элементы.
"""
'''
colors = {'red', 'green', 'blue'}
print(colors)          # {'red', 'blue', 'green'}
# Добавляем элемент
colors.add('gray')     
print(colors)          # {'red', 'blue', 'green', 'gray'}
# Удаляем элмент
colors.remove('red') 
print(colors)          # {'green', 'gray', 'blue'}
colors.discard('red')  # Если есть значения, то удаляет. Если нет, то пропускает
print(colors)          # {'green', 'gray', 'blue'}
# Удаляем все элементы
colors.clear()
print(colors)          # set()
'''

# Операции со множествами
'''
a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
# копируем
с = a.copy()            # {1, 2, 3, 5, 8}
# объединяем
u = a.union(b)          # {1, 2, 3, 5, 8, 13, 21}
# находим пересечение
i = a.intersection(b)   # {8, 2, 5}
# Разность 'a - b'
dl = a.difference(b)    # {1, 3}
# Разность 'b - a'
dr = b.difference(a)    # {13, 21}
# разность 
q = a.union(b).difference(a.intersection(b)) # {1, 21, 3, 13}
'''

# Замороженное множества "frozenset"
'''
a = {1, 8, 6}
b = frozenset(a)
print(b)            # frozenset({8, 1, 6})
'''
"""

### ГЕНЕРАТОР СПИСКА

# Cоздать список, состоящий из четных чисел 
# 1) в диапазоне от 1 до 100
'''
list_1 = []
for i in range(1, 101):
    list_1.append(i)
print(list_1)
# Запишем решение сокращенно(c помощью генератора списка)
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


