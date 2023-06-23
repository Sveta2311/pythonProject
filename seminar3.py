# Задача №1

# Вручную создайте список с целыми числами, которые повторяются. Получите новый список, который содержит
# уникальные (без повтора) элементы исходного списка. *Подготовьте два решения, короткое и длинное, которое
# не использует другие коллекции помимо списков.

# Способ первый

# myList = [1, 2, 3, 4, 5, 6, 7, 8, 8, 8, 5, 5, 6, 6, 8, 8, 7, 2, 6, 1]
# print(myList)
# myNewList = []
# for i in myList:
#     if i not in myNewList: myNewList.append(i)
# print(myNewList)

# Способ второй
# myList = [1, 2, 3, 4, 5, 6, 7, 8, 8, 8, 5, 5, 6, 6, 8, 8, 7, 2, 6, 1]
# myNewList2 = list(set(myList))  # Но тут используется множ-во
# print(myNewList2)

# Задача №2

# Пользователь вводит данные. Сделайте проверку данных
# и преобразуйте, если возможно в один из вариантов ниже:
# целое положительное число,
# вещественное положительное или отрицательное число,
# строку в нижнем регистре, если в строке есть
# хотя бы одна заглавная буква.
# Строку в нижнем регистре в остальных случаях.

# sentence = (input(' -> '))
# if sentence.isdecimal() : print(int(sentence))
# elif sentence[0] in '-0123456789' and sentence.count('.') in range(0,2) and sentence[1:].replace('.','').isdecimal():
#     print(float(sentence))
# elif sentence.isupper() : print(sentence.isupper())
# else: print(sentence.islower())

# isnumeric() - возвращает True , если все символы в строке являются числовыми символами,
# и есть по крайней мере один числовой символ (строка является не пустой и не состоит из пробелов),
# False в противном случае.

# Задача №3

# Создайте вручную кортеж содержащий элементы разных типов. Получите из него словарь списков, где: ключ — тип элемента,
# значение — список элементов данного типа.

# myTuple = (1, 2.3, 'hi', True, 'Hello', 5)
# myDict = {}
# myList = list(myTuple)
#
# for i in myList:
#     if type(i) in myDict.keys() : myDict[type(i)].append(i)
#     else:
#         myValue = []
#         myValue.append(i)
#         myDict[type(i)] = myValue
# print(myDict)       # можно так вывести,
# for key in myDict:
#     print(f"type: {key}  value: {myDict[key]} ")    # а можно перебрать попарно

# Задача №4

# Создайте вручную список с повторяющимися элементами. Удалите из него все элементы, которые встречаются дважды.

# myList = [1, 2, 3, 4, 5, 6, 7, 8, 8, 8, 5, 5, 6, 6, 8, 8, 7, 2, 6, 1]
# for i in myList:
#     if myList.count(i) > 1:
#         for j in myList:
#             myList.remove(j)            # Удалим копии
#     #myList.remove(i)                 #Эта строка удалит и уникальные и копии
# print(myList)

# Задача №5

# Создайте вручную список с повторяющимися целыми числами.
# Сформируйте список с порядковыми номерами нечётных элементов исходного списка. Нумерация начинается с единицы

# def odd(x):
#     if x == 0 : odd = True
#     elif x % 2 == 0: odd = True
#     else : odd = False
#     return odd
#
# myList = [1, 2, 3, 4, 5, 6, 7, 8, 8, 8, 5, 5, 6, 6, 8, 8, 7, 2, 6, 1]
# myNewList = []
# for i in range(len(myList)):
#     if not odd(myList[i]): myNewList.append(i+1)
# print(myNewList)

# Задача №6

# Пользователь вводит строку текста. Вывести каждое слово с новой строки. Строки нумеруются начиная с единицы.
# Слова выводятся отсортированными, согласно кодировки Unicode. Текст выравнивается по правому краю так,
# чтобы у самого длинного слова был один пробел между ним и номером строки.

# sentence = str(input('Тут строка текста -->>> '))
# myList = sentence.split(' ')
# myList.sort()
# count = 1
# for i in myList:
#     i = str(count)+' ' + str(i)
#     print(str(i).rjust(50, '*'))
#     count += 1

# Задача №7

# Пользователь вводит строку текста. Подсчитайте, сколько раз встречается каждая буква в строке без использования
# метода count и с ним. Результат сохраните в словаре, где ключ — символ, а значение — частота встречи
# символа в строке. Обратите внимание на порядок ключей. Объясните почему они совпадают или не совпадают в ваших решениях.

# Способ первый

# sentence = str(input('Сюда предложение ->>> '))
# myDict = {}
# for i in set(sentence):
#     myDict[i] = sentence.count(i)
# print(myDict)

# Способ второй

# sentence = str(input('Сюда предложение ->>> '))
# myDict = {}
# myNewDict = dict((i, sentence.count(i)) for i in set(sentence))
# print(myNewDict)

# Задача №8

# Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей. Ответьте на вопросы:
# Какие вещи взяли все три друга. Какие вещи уникальны, есть только у одного друга. Какие вещи есть у всех друзей кроме одного
# и имя того, у кого данная вещь отсутствует. Для решения используйте операции с множествами. Код должен расширяться
# на любое большее количество друзей.

# def addFriend(group):
#     name = str(input('Имя друга - '))
#     scarb = tuple((str(input('Что у него в рюкзаке - '))).split(' '))
#     group[name] = scarb
#     return group
#
# group = {'Андрюха': ('нож','ложка','тарелка', 'палатка'), 'Васятка': ('хлеб','нож','ложка','тарелка'), 'Руслан': ('нож','тарелка','котелок','мафон')}
# print(group)
# # addFriend(group)   #друго - добавлялка
# persons = group.keys()
# habar = group.values()
#
# myList = []
# for key in group:
#     myList.extend(list(group[key]))
#
# notUniqueItem = set()
# notHaveOne = set()
# for key, value in group.items():
#     for i in range(len(value)):
#         if myList.count(value[i]) == 1 : print(f'{value[i]} - уникальный предмет {key} притащил его')
#         if myList.count(value[i]) == len(group) :
#             #print(f'{value[i]} - есть у всех')
#             notUniqueItem.add(value[i])
#         if myList.count(value[i]) == len(group) - 1 : notHaveOne.add(value[i])
# for key, value in group.items():
#     for i in notHaveOne:
#         if i not in group[key] :
#             print(f'{key} не взял с собой {i}, ну чокнутый :)')
# print(f'Есть у всех {notUniqueItem}')

# Вариант с урока:

# group = {'Андрюха': ('нож','ложка','тарелка', 'палатка'), 'Васятка': ('хлеб','нож','ложка','тарелка'), 'Руслан': ('нож','тарелка','котелок','мафон')}
# print(group)
#
# x = set(group['Андрюха'])
# y = set(group['Васятка'])
# z = set(group['Руслан'])
# sum = x|y
# sum = sum|z
# print(sum)
# print(z.difference(y))

# Задача 1 ДЗ

# Дан список повторяющихся элементов. Вернуть список
# с дублирующимися элементами. В результирующем списке
# не должно быть дубликатов.

# myList = [2, 6, 1, 8, 8, 1, 2, 5, 53, 4, 5, 6, 7, 8, 8, 8, 5, 5, 6, 6, 8, 8, 7, 2, 6, 1]
# print(myList)
# myNewList = []
# for i in myList:
#     if i not in myNewList:
#         if myList.count(i) > 1:
#             myNewList.append(int(i))
# print(f"Cписок с дублирующимися элементами: {myNewList}")

# Задача 2 ДЗ

# В большой текстовой строке подсчитать количество встречаемых
# слов и вернуть 10 самых частых. Не учитывать знаки препинания
# и регистр символов. За основу возьмите любую статью
# из википедии или из документации к языку.

# data = open(r"text.txt", "r", encoding="UTF-8")
# text = data.read()
# data.close()
# delete = '.,!?;:-[]{}()='
# newText = [i.rstrip(delete).lower() for i in text.split() if len(i.rstrip(delete)) > 1]
# print(*sorted(set(newText), key=newText.count, reverse=True)[:10], sep='\n')

# Задача 3 ДЗ

# Создайте словарь со списком вещей для похода в качестве
# ключа и их массой в качестве значения. Определите, какие
# вещи влезут в рюкзак, передав его максимальную
# грузоподъёмность. Достаточно вернуть один допустимый вариант.

# things = {'зажигалка': 20, 'компас': 100, 'фрукты': 500, 'рубашка': 300,
#           'термос': 1000, 'аптечка': 200, 'куртка': 600, 'бинокль': 400, 'удочка': 1200,
#           'салфетки': 40, 'бутерброды': 820, 'палатка': 5500, 'спальный мешок': 2250, 'жвачка': 10}
# ves = int(input('Введите максимальную грузоподъёмность рюкзака: '))
# temp_w = 0
# temp_things = []
# sorted_things = dict(sorted(things.items(), key=lambda x: -x[1]))
#
# for k, v in sorted_things.items():
#     if temp_w + v <= ves:
#         temp_w = temp_w + v
#         temp_things.append(k)
#
# print(temp_things)
