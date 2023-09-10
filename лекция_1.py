'''
print(5, 8, 6)
int   - целые числа
float - Дробные числа
bool  - Логический тип данных(True/False)
str   - Строка
'''
'''
n = None  #  - пустое значение
n = 1.89  #  - Дробные числа
n = 5     #  - целые числа
n = 'dfd' #  - Строка
'''

# n = 'fd\'df'   # | -> fd'df
# print(type(n))
'''
a = 5
b = 5.89
c = 'hello'

print(a,'-', b, '-', c)
print(f'{a} - {b} - {c}')
print('{} - {} - {}'.format(a,b,c))
'''

# Ввод данных 
'''
print('Введите первую строку: ')
a = input()
b = input('Введите вторую строку: ')
print(a, '+', b, '=', a + b)           # -> 23 + 23 = 2323
'''
'''
print('Введите первую строку: ')
a = int(input())
b = int(input('Введите вторую строку: '))
print(a, '+', b, '=', a + b)           # -> 23 + 23 = 46
'''

# +   - сложение
# -   - Вычитание
# *   - Умножение
# /   - Деление
# %   - Остаток от деление
# //  - Целечисленное деление
# **  - Возведение в степень

# Округление:
'''
a = 5.89956
b = 6.5656
print(a*b)           # -> 38.734151136
print(round(a*b, 2)) # -> 38.73
'''

# Cокращение записи:
'''
iter = 2    
iter += 3   # iter = iter + 3
iter -= 4   # iter = iter - 4
iter *= 5   # iter = iter * 5
iter /= 5   # iter = iter / 5
iter //= 5  # iter = iter // 5
iter %= 5   # iter = iter % 5
iter **= 5  # iter = iter ** 3
'''

# Логические операции:
'''
>   # - больше
>=  # - больше или равно
<   # - меньше
<=  # - меньше или равно
==  # - равно
!=  # - не равно
not # - Не (отрицание)
and # - и (конъюнкция)
or  # - или (дизъюнкция)
'''
'''
username = input('Введите имя: ')
if username == 'Маша':
    print('Ураа, это же Маша!!!')
elif username == 'Марина':
    print('Я так ждала вас, Марина!')
elif username == 'Ильнар':
    print('Ильнар - топ')
else:
    print('Привет, ', username)
'''

# Вложенные циклы
'''
line = ''
for i in range(5):
    line = ' '
    for j in range(5):
        line += '*'
    print(line)           
'''

# Cтрока:
'''
text = 'СъЕШЬ еще этих МяГкИх французских булок'

print(len(text))                       # -> 39
print('еще' in text)                   # -> True
print(text.lower())                    # -> съешь еще этих мягких французских булок
print(text.upper())                    # -> СЪЕШЬ ЕЩЕ ЭТИХ МЯГКИХ ФРАНЦУЗСКИХ БУЛОК
print(text.replace('еще', 'ЕЩЕ'))      # -> СъЕШЬ ЕЩЕ этих МяГкИх французских булок
print(text[0])                         # -> С
print(text[1])                         # -> ъ
print(text[len(text)-1])               # -> к
print(text[-5])                        # -> б
print(text[:])                         # -> СъЕШЬ еще этих МяГкИх французских булок
print(text[:2])                        # -> Съ
print(text[len(text)-2:])              # -> ок
print(text[2:9])                       # -> ЕШЬ еще
print(text[6:-18])                     # -> еще этих МяГкИх
print(text[0:len(text):6])             # -> Сеикакл
print(text[::6])                       # -> Сеикакл
text = text[2:9] + text[-5] + text[:2] # -> ЕШЬ ещебСъ
print(text)
'''



