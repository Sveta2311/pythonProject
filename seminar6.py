# Задача 1

# Вспомните какие модули вы уже проходили на курсе.
# Создайте файл, в котором вы импортируете встроенные в модуль функции под псевдонимами. (3-7 строк импорта).


import sys as s

import random as rn

import math as mt

import time as tm

from sys import argv as ar

from random import randint as rd

from math import sqrt as sq

from time import time as t

# print(rd(0, 10))

# Задача 2

# Создайте модуль с функцией внутри.
# Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток.
# Внутри генерируется случайное число в указанных границах и пользователь должен угадать его за заданное число попыток.
# Функция выводит подсказки “больше” и “меньше”. Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.

# def function(a, b, c):
#    n = rd(a, b)
#    print(n)
#    while c > 0:
#       chislo = int(input('Введите число: '))
#       if chislo > n:
#          print('Число меньше')
#          c -= 1
#       elif chislo < n:
#          print('Число больше')
#          c -= 1
#       else:
#          print('Угадали число')
#          return True
#          break
#    print('Не угадали число')
#    return False


# function(0, 10, 3)

# Задача 3

# Улучшаем задачу 2. Добавьте возможность запуска функции “угадайки” из модуля в командной строке терминала.
# Строка должна принимать от 1 до 3 аргументов: параметры вызова функции.
# Для преобразования строковых аргументов командной строки в числовые параметры используйте генераторное выражение.

# if __name__ == '__main__':
#    flname, *param = ar
#    # function(*(int(n) for n in param))
#    print(function(*(int(n) for n in param)))
#    print(flname)

# Задача 4

# Создайте модуль с функцией внутри.
# Функция получает на вход загадку, список с возможными вариантами отгадок и количество попыток на угадывание.
# Программа возвращает номер попытки, с которой была отгадана загадка или ноль, если попытки исчерпаны.

# def zagadka(zag, otg, popit):
#     print(zag)
#     count = 1
#     while count <= popit:
#         otvet = input('Ваш ответ: ').lower()
#         if otvet in otg:
#             print(f'Угадали c {count} попытки')
#             return count
#         else:
#             print('Попробуйте еще раз')
#             count += 1
#     print('Не угадали')
#     return 0
#
# # Либо:
#
# myDict = {'Идет шуршит': ['шурашанчик'],
#                           'В кармане на П начинается': ['путылка'],
#                           'В кармене на Ы начинается': ['ышо одна путылка']}
# for i in myDict:
#     zagadka(i, myDict[i], 3)
#
# zagadka('Висит груша, нельзя скушать?', ['лампочка', 'лампа', 'лампомпулечка'], 3)

# Задача 5

# Добавьте в модуль с загадками функцию, которая хранит словарь списков.
# Ключ словаря - загадка, значение - список с отгадками.
# Функция в цикле вызывает загадывающую функцию, чтобы передать ей все свои загадки.

# def archiv():
#     myDict = {'Зимой и летом одним цветом': ['ель', 'елка', 'доллар'], 'Висит груша - нельзя скушать': ['груша', 'игрушка', 'лампочка']}
#
#     for key, values in myDict.items():
#         zagadka(key, values, rn.randint(1, 5))


# Задача 6

# Добавьте в модуль с загадками функцию, которая принимает на вход строку (текст загадки) и число (номер попытки, с которой она угадана).
# Функция формирует словарь с информацией о результатах отгадывания.
# Для хранения используйте защищённый словарь уровня модуля.
# Отдельно напишите функцию, которая выводит результаты угадывания из защищённого словаря в удобном для чтения виде.
# Для формирования результатов используйте генераторное выражение.

# _solutions = {}  # словарь protected (защищенный)
# myDict = {'Зимой и летом одним цветом': ['ель', 'елка', 'доллар'], 'Висит груша - нельзя скушать': ['груша', 'игрушка', 'лампочка']}
#
#
# def logAnswers(zag: str, popit: int):
#     num = zag(zag, myDict[zag], popit)
#     _solutions[zag] = [num, True if num else False]
#
#
# def printDict():
#     for k, v in _solutions.items():
#         print(k, v)

# Задача 7

# Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
# Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне [1, 9999].
# Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
# Проверку года на високосность вынести в отдельную защищённую функцию.

# def calendar(date: str):
#     day, month, year = map(int, date.split('.'))
#     if 1 <= year <= 9999:
#         if month in [1, 3, 5, 7, 8, 10, 12] and 1 <= day <= 31:
#             return True
#         elif month in [4, 6, 9, 11] and 1 <= day <= 30:
#             return True
#         elif 1 <= day <= 28 + is_visokos_year(year):
#             return True
#         else:
#             return False
#     return False
#
#
# def is_visokos_year(year):
#     return year % 4 == 0 and year % 100 != 0 or year % 400 == 0