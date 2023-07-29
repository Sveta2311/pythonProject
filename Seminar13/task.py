# Задача 1

# Создайте функцию, которая запрашивает числовые данные от
# пользователя до тех пор, пока он не введёт целое или
# вещественное число.
# Обрабатывайте не числовые данные как исключения.

# def chislo():
#     while True:
#         num = input('Введите целое число: ')
#         try:
#             num = float(num)
#             return num
#         except:
#             print('Введите целое или вещественное число!')
#
# print(chislo())

# Задача 2

# Создайте функцию аналог get для словаря.
# Помимо самого словаря функция принимает ключ и
# значение по умолчанию.
# При обращении к несуществующему ключу функция должна
# возвращать дефолтное значение.
# Реализуйте работу через обработку исключений.

# def myGet(dict, key, defaultValue):
#     try:
#         value = dict[key]
#     except:
#         value = defaultValue
#     return value
#
# dict1 = {1:7, 5:4, 8:1}
#
# print(myGet(dict1, 5, 0))
# print(myGet(dict1, 15, 0))

# Задача 3

# Создайте класс с базовым исключением и дочерние классы исключения:
# ○ ошибка уровня,
# ○ ошибка доступа.

import json


class Iscl(Exception):
    pass
class Dochiscl(Iscl):
    pass
class Dochiscl1(Iscl):
    pass

class Robot:
    def __init__(self, name, model):
        self.name = name
        self.model = model


with open("new_user.json", "r", encoding="utf-8") as nn:
    nn = json.load(nn)
    print(nn)

    list = []

    for i in nn:
        print(nn[i])

        rbt = Robot(i, nn[i])
        list.append(rbt)

    for r in list:
        print(r.name, r.model)


    while True:

        p1 = int(input('Введите одно число: '))
        p2 = int(input('Введите второе число: '))

        try:

            list[p1]
            list[p2]
            break
        except:
            print("Ввели не то число!")

    a = list[p1]
    b = list[p2]

    if a.model > b.model:
        print(a.name)
    else:
        print(b.name)

# while True:
#     try:
#         p1 = int(input("input 1: "))
#         a = myList[p1]
#         break
#     except:
#         print("input 1 again")
#
# while True:
#     try:
#         p2= int(input("input 2: "))
#         b = myList[p2]
#         break
#     except:
#         print("input 2 again")










