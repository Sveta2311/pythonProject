# Задача №1

# Пользователь вводит произвольно строку из четырёх
# или более целых чисел, разделённых символом “/”.
# Сформируйте словарь, где:
# второе и третье число являются ключами,
# первое число является значением для первого ключа,
# четвертое и все возможные последующие числа
# хранятся в ввиде кортежа, как значения второго ключа.

# Варант 1

# text = '1/2/3/4/5/6/7/8'
# text = text.split('/')
# print({text[1]:text[0], text[2]:tuple(i for i in text if int(i)>3)})

# Вариант в одну строчку, как на лекции

# one, two, three, *other = input('Какой текст преобразовать? ').split('/')

# Вариант 2

# list_value_and_key = input('Введите значения, используя "/" для разделения').split('/')
# list_value_and_key = list(filter(None, list_value_and_key))
# list_value_and_key = [int(item) for item in list_value_and_key]
#
# list_key = [list_value_and_key[i] for i in range(1, 3)]
# list_value = [list_value_and_key[0],
#               tuple(list_value_and_key[i] for i in range(3, len(list_value_and_key)))]
#
# list_dict = dict(zip(list_key, list_value))
# print(list_dict)

# Вариант 3

# list_value_and_key = [int(item) for item in
#                       list(filter(None, input('Введите значения, '
#                                               'используя "/" для разделения ').split('/')))]
#
# print(dict(zip([list_value_and_key[i] for i in range(1, 3)],
#                      [list_value_and_key[0],
#                       tuple(list_value_and_key[i] for i in range(3, len(list_value_and_key)))])))

# Задача №2

# Самостоятельно сохраните в переменной строку текста.
# Создайте из строки словарь, где ключ — буква, а значение — код буквы.
# Напишите преобразование в одну строку.

# Вариант 1

# print(dict(zip(list('абвгдеёжзийклмнопрст'),
#                [item.encode('utf-8') for item in list('абвгдеёжзийклмнопрст')])))

# Вариант 2

# text = 'Самоедлинноеслововрусскомсловаре'
# print(f'{({text[i]:ord(text[i]) for i in range(len(text))})}')

# Задача №3

# Продолжаем развивать задачу 2.
# Возьмите словарь, который вы получили.
# Сохраните его итераторатор.
# Далее выведите первые 5 пар ключ-значение,
# обращаясь к итератору, а не к словарю.

# list_dict = dict(zip(list('абвгдеёжзийклмнопрст'),
#                      [item.encode('utf-8') for item in list('абвгдеёжзийклмнопрст')]))
#
# list_dict_iter = iter(list_dict)
#
# for i in range(5): print(next(list_dict_iter))

# Задача №4

# Создайте генератор чётных чисел от нуля до 100.
# Из последовательности исключите
# числа, сумма цифр которых равна 8.
# Решение в одну строку.

# Вариант 1

# print(f'{list(i for i in range(2, 100, 2) if sum(int(j) for j in str(i) )!=8)}')

# Вариант 2 (с повторами, генератор случайных чисел)

# import random; print([random.randrange(2, 100, 2) for i in range(100) if sum(int(j) for j in str(i)) != 8])

# Вариант 3 (без повторов)

# print([i for i in range(2, 100, 2) if sum(int(j) for j in str(i)) != 8])

# Задача №5

# Напишите программу, которая выводит
# на экран числа от 1 до 100.
# При этом вместо чисел, кратных трем,
# программа должна выводить слово «Fizz»
# Вместо чисел, кратных пяти — слово «Buzz».
# Если число кратно и 3, и 5, то программа
# должна выводить слово «FizzBuzz».
# *Превратите решение в генераторное выражение.

# print([(((i,'Fedd')[i%3==0],'Buzz')[i%5==0],'FeedBuzz')[i%15==0] for i in range(1, 100)])

# Задача №6

# Выведите в консоль таблицу умножения
# от 2х2 до 9х10 как на школьной тетрадке.
# Таблицу создайте в виде однострочного
# генератора, где каждый элемент генератора —
# отдельный пример таблицы умножения.
# Для вывода результата используйте «принт»
# без перехода на новую строку.

# Вариант в одну строчку.

# print('\n'.join(''.join(f'{j} * {i} = {i * j}\t' for i in range(2, 10)) for j in range(2, 10)))

# LOWER_LIMIT = 2
# UPPER_LIMIT = 10
# COLUMN = 4

# for j in range(2, 10): print([f'{j} * {i} = {i * j}' for i in range(2, 10)])
#
# table = (f'{k:>2} x {j:>2} = {k * j:>2}\t'
#          if k != i + COLUMN - 1
#             else f'{k:>2} x {j:>2} = {k * j:>2}\n'
#                 if j != UPPER_LIMIT else f'{k:>2} x {j:>2} = {k * j:>2}\n\n'
#                     for i in range(LOWER_LIMIT, UPPER_LIMIT, COLUMN)
#                         for j in range(LOWER_LIMIT, UPPER_LIMIT + 1)
#                             for k in range(i, i + COLUMN))

# Комментарий от преподавателя

# LOWER_LIMIT = 2
# UPPER_LIMIT = 10
# COLUMN = 4

# table = (f'{k:>2} x {j:>2} = {k * j:>2}\t'
#     if k != i + COLUMN - 1
#         else f'{k:>2} x {j:>2} = {k * j:>2}\n'
#             if j != UPPER_LIMIT
#                 else f'{k:>2} x {j:>2} = {k * j:>2}\n\n'
#                     for i in range(LOWER_LIMIT, UPPER_LIMIT, COLUMN)
#                         for j in range(LOWER_LIMIT, UPPER_LIMIT + 1)
#                             for k in range(i, i + COLUMN))

# Задача №7

# Создайте функцию-генератор.
# Функция генерирует N простых чисел,
# начиная с числа 2.
# Для проверки числа на простоту используйте
# правило: «число является простым, если делится
# нацело только на единицу и на себя».

# def is_prime(x):
#     for i in range(2, int((x**0.5)+1)):
#         if x % i == 0:
#             return False
#     return True
#
# def gener_integer(x):
#     count = 1
#     prime_number = 2
#     yield prime_number
#     while count < x:
#         prime_number += 1
#         if is_prime(prime_number):
#             count += 1
#             yield prime_number
#
# print([i for i in gener_integer(100)])

# Через библиотеку с перебором до 100

# from sympy import *;
# print([i for i in range(100) if isprime(i)])

# Задача 1 ДЗ

# Напишите функцию, которая принимает на вход строку —
# абсолютный путь до файла. Функция возвращает кортеж из трёх
# элементов: путь, имя файла, расширение файла.

# import os
#
# string = "C:/Users/Shark/PycharmProjects/pythonProject/seminar5.py"
#
#
# def fun(f_path: str) -> tuple:
#     path, filename = os.path.split(f_path)
#     name, extension = filename.split('.')
#     return path, name, extension
#
#
# print(f'Кортеж из трех элементов (путь, имя файла, расширение файла): \n{fun(string)}')

# Задача 2 ДЗ

# Напишите однострочный генератор словаря, который принимает
# на вход три списка одинаковой длины: имена str, ставка int,
# премия str с указанием процентов вида «10.25%». В результате
# получаем словарь с именем в качестве ключа и суммой
# премии в качестве значения. Сумма рассчитывается
# как ставка умноженная на процент премии.

# names = ['Лена', 'Света', "Маша"]
# rates = [18000, 19000, 20000]
# awards = ['10.0%', '7.25%', '5%']
# print({name: rate * float(award[:-1]) / 100 for name, rate, award in zip(names, rates, awards)})

# Задача 3 ДЗ
# Создайте функцию генератор чисел Фибоначчи (элементы числовой последовательности,
# в которой первые два числа равны 0 и 1, а каждое последующее число равно сумме двух предыдущих чисел).

# a = int(input('Введите число, количество чисел Фибоначчи: '))
#
#
# def fibonacci(n):
#     a, b = 0, 1
#     for _ in range(n):
#         yield a
#         a, b = b, a + b
#
#
# print(f'Числа Фибоначчи: {list(fibonacci(a))}')
