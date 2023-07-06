# Задача 1
from os import chdir
from pathlib import Path
# Напишите функцию, которая заполняет файл
# (добавляет в конец) случайными парами чисел.
# Первое число int, второе - float разделены вертикальной чертой.
# Минимальное число - -1000, максимальное - +1000.
# Количество строк и имя файла передаются как аргументы функции.

# from random import randint, uniform
#
# MIN = -1000
# MAX = 1000
#
#
# def random_numbers(numb, name):
#     with open(name, "a", encoding="utf-8") as f:
#         for _ in range(numb):
#             n1 = randint(MIN, MAX)
#             n2 = uniform(MIN, MAX)
#             f.write(f'{n1} | {n2} \n')
#
#
# numb = 4
# name = "fl.txt"
# random_numbers(numb, name)

# Задача 2

# Напишите функцию, которая генерирует псевдоимена.
# Имя должно начинаться с заглавной буквы,
# состоять из 4-7 букв, среди которых
# обязательно должны быть гласные.
# олученные имена сохраните в файл.

# from random import randint, choice
#
#
# DIC1 = "AIEYUO"
# DIC2 = "QWRTPSDFHGKL"
# RAND = 15
#
# def names():
#     with open("filik.txt", "a", encoding="utf-8") as f:
#         for i in range(RAND):
#             name = ""
#             for i in range(randint(2, 4)):
#                 name += choice(DIC1)
#                 if len(name) >= 7: break
#                 name += choice(DIC2)
#             f.write(f'{name} \n')
#
# names()

# Задача 3

# Напишите функцию, которая открывает на чтение созданные
# в прошлых задачах файлы с числами и именами.
# Перемножьте пары чисел. В новый файл сохраните имя и произведение:
# если результат умножения отрицательный, сохраните имя,
# записанное строчными буквами и произведение по модулю,
# если результат умножения положительный, сохраните имя
# прописными буквами и произведение округлённое до целого.
# В результирующем файле должно быть столько же строк,
# сколько в более длинном файле.
# При достижении конца более короткого файла,
# возвращайтесь в его начало.

# from random import randint, choice
#
# DIC1 = "AIEYUO"
# DIC2 = "QWRTPSDFHGKL"
#
#
# def mult():
#     with (
#         open('fl.txt', 'r', encoding='utf-8') as numbers,
#         open('filik.txt', 'r', encoding='utf-8') as liter,
#         open('result', 'a', encoding='utf-8') as r
#     ):
#         while res_n := numbers.readline():
#             a = res_n.replace(' \n', '').split(" | ")
#
#             if a == ['\n']:
#                 continue
#             print(a)
#             mult_ = int(a[0]) * float(a[1])
#             if mult_ < 0:
#                 res_l = liter.readline().replace(' \n', '')
#                 r.write(f'{res_l.lower(), abs(mult_)} \n')
#             elif mult_ >= 0:
#                 r.write(f'{res_l.upper(), round(mult_)} \n')
#
# mult()

# Задача 4

# Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:\
# расширение,
# минимальная длина случайно сгенерированного имени, по умолчанию 6,
# максимальная длина случайно сгенерированного имени, по умолчанию 30,
# минимальное число случайных байт, записанных в файл, по умолчанию 256,
# максимальное число случайных байт, записанных в файл, по умолчанию 4096,
# количество файлов, по умолчанию 42.
# Имя файла и его размер должны быть в рамках переданного диапазона.

# from random import randint, choice
#
# DIC1 = "AIEYUO"
# DIC2 = "QWRTPSDFHGKL"
#
#
# def function(text, a=5, b=30, c= 7, d=256, n = 42):
#     for _ in range(n):
#         name = ""
#         for i in range(randint(6, 30)):
#             name += choice(DIC1)
#             if len(name) >= 30: break
#             name += choice(DIC2)
#         name = name + '.' + text
#         with open(name, 'w', encoding='utf-8') as new_f:
#             g = bytes(randint(0, 255) for i in range(randint(256, 4096)))
#             new_f.write(f'{g}')
#
#
# function("txt", a=5, b=30, c= 7, d=256, n = 42)

# Задача 5

# Доработаем предыдущую задачу.
# # Создайте новую функцию которая генерирует файлы с разными расширениями.
# # Расширения и количество файлов функция принимает в качестве параметров.
# # Количество переданных расширений может быть любым.
# # Количество файлов для каждого расширения различно.
# # Внутри используйте вызов функции из прошлой задачи.

# from random import randint, choice
#
# DIC1 = "AIEYUO"
# DIC2 = "QWRTPSDFHGKL"
#
#
# def function(dic, a=5, b=30, c=7, d=256):
#     for key in dic:
#         for _ in range(dic[key]):
#             name = ""
#             for i in range(randint(6, 30)):
#                 name += choice(DIC1)
#                 if len(name) >= 30: break
#                 name += choice(DIC2)
#             name = name + '.' + key
#             with open(name, 'w', encoding='utf-8') as new_f:
#                 g = bytes(randint(0, 255) for i in range(randint(256, 4096)))
#                 new_f.write(f'{g}')
#
#
# dic = {"txt": 5, "doc": 3}
# function(dic, a=5, b=30, c=7, d=256)

# Задача 6

# Дорабатываем функции из предыдущих задач.
# Генерируйте файлы в указанную директорию — отдельный параметр функции.
# Отсутствие/наличие директории не должно вызывать ошибок в работе функции
# (добавьте проверки).
# Существующие файлы не должны удаляться/изменяться в случае совпадения имён.

# from random import randint, choice
#
# DIC1 = "AIEYUO"
# DIC2 = "QWRTPSDFHGKL"
#
#
# def function(dic, a=5, b=30, c=7, d=256):
#     for key in dic:
#         for _ in range(dic[key]):
#             name = ""
#             for i in range(randint(6, 30)):
#                 name += choice(DIC1)
#                 if len(name) >= 30: break
#                 name += choice(DIC2)
#             name = name + '.' + key
#             if Path(name).is_file():
#                 continue
#             with open(name, 'w', encoding='utf-8') as new_f:
#                 g = bytes(randint(0, 255) for i in range(randint(256, 4096)))
#                 new_f.write(f'{g}')
#
#
# dic = {"txt": 5, "doc": 3}
# function(dic, a=5, b=30, c=7, d=256)
#
# def dir(text):
#     if isinstance(text, str):
#         a = Path(text)
#     else:
#         a = text
#     if not a.is_dir():
#         a.mkdir(parents=True)
#     chdir(a)
#     function(dic, a=5, b=30, c=7, d=256)
#
# dir('Sem7')

# Задача 7

# Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п..
# Каждая группа включает файлы с несколькими расширениями.
# В исходной папке должны остаться только те файлы, которые не подошли для сортировки.

# def sort_file(dict_file_extension, dir_name):
#     if isinstance(dir_name, str):
#         dir_name = Path(dir_name)
#     else:
#         dir_name = dir_name
#     chdir(dir_name)
#     for key in dict_file_extension:
#         a = Path(key)
#         if not a.is_dir():
#             a.mkdir(parents=True)
#
#     p = Path(Path().cwd())
#     for obj in p.iterdir():
#         for key in dict_file_extension:
#             if obj.suffix in dict_file_extension[key]:
#                 obj.replace(p / key / obj.name)
#
# put = 'C:/'
# dict_file_extension = {'video': ['.mov', '.avi', '.doc', '.mp4'], 'docum': ['.txt']}
# sort_file(dict_file_extension, put)
