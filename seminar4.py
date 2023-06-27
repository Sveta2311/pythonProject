# Задача №1

# Напишите функцию, которая принимает строку текста.
# Вывести функцией каждое слово с новой строки.
# Строки нумеруются начиная с единицы.
# Слова выводятся отсортированными согласно кодировки Unicode.
# Текст выравнивается по правому краю так, чтобы у самого
# длинного слова был один пробел между ним и номером строки.

# def textPrinting(text, count, lenMaxWord):
#     print(count, text.rjust(lenMaxWord, '-'))
# def superFunc(text):
#     text = "".join([i for i in text.lower() if i.isalpha() or i == " "])
#     myWords = sorted(text.split(' '))
#     count = 1
#     lenMaxWord = len(max(myWords, key=len))  # Длина макс. слова. Чтобы не поплыл текст при выводе
#     for i in myWords:
#         textPrinting(i, count, lenMaxWord)
#         count += 1
#
# text = 'пивная, еще парочку..., Эй ты, дай папироску, у тебя штаны в полоску'
# superFunc(text)

# Задача №2

# Напишите функцию, которая принимает строку текста.
# Сформируйте список с уникальными кодами Unicode каждого
# символа введённой строки отсортированный по убыванию.

# def textUnicode(text):
#     uniList = []
#     text = list(text)
#     text.sort(reverse = True)
#     print(text)
#     for i in text :
#         uniList.append(ord(i))
#     return uniList
#
# text = 'пивная, еще парочку..., Эй ты, дай папироску, у тебя штаны в полоску'
# print(text)
# text = "".join([i for i in text.lower() if i.isalpha() or i ==" "]).replace(' ','')
# print(set(textUnicode(text)))

# Задача №3

# Функция получает на вход строку из двух чисел через пробел.
# Сформируйте словарь, где ключом будет
# символ из Unicode, а значением — целое число.
# Диапазон пар ключ-значение от наименьшего из введённых
# пользователем чисел до наибольшего включительно.

# def dictUnicode(numIn):
#     numIn = list(map(int, numIn.split(' ')))
#     maxN = max(numIn)
#     minN = min(numIn)
#     for i in range(minN, maxN + 1):
#         myDict[chr(i)] = i
#     return myDict
# numIn = input('вводим два числа через пробел')
# myDict = {}
#
# print(dictUnicode(numIn))

# Задача №4

# Функция получает на вход список чисел.
# Отсортируйте его элементы in place без использования встроенных в язык сортировок.
# Как вариант, напишите сортировку пузырьком.
# Её описание есть в википедии.

# Вариант 1.

# def create_list():  # Создаем последовательность и помещаем в список
#     print('С клавиатуры введите список элементов(числа), по окончанию ввода нажмите Enter')
#     new_list = []
#     while True:
#         try:
#             element = int(input('> '))
#             int(element)
#             new_list.append(element)
#         except:
#             break
#     return new_list
#
# def sort_bubble(sort_list):  # Сортируем по возрастанию
#     for i in range(0, len(sort_list)):
#         for j in range(0, len(sort_list) - i - 1):
#             if sort_list[j] > sort_list[j + 1]:
#                 sort_list[j], sort_list[j + 1] = sort_list[j + 1], sort_list[j]
#     return sort_list
#
# def main():
#     new_list = create_list()
#     print(new_list)
#     if len(new_list) == 0:
#         print('Отсутствуют числовые элементы в списке')
#         exit()
#     sort_list = sort_bubble(new_list)
#     print(sort_list)
#
# main()

# Вариант 2.

# def superSort(myList):
#     for i in range (len(myList)):
#         for j in range(i, len(myList)):
#             if i == j : continue
#             elif myList[i] > myList[j] :
#                 myList[i], myList[j] = myList[j], myList[i]
#     return myList
# myList = [6, 3, 1, 2, 5, 7, 8, 2, 5, 2, 5, 7, 7, 9, 1, 0, 9, 1, 3, 4]
# print(superSort(myList))

# Задача №5

# Функция принимает на вход три списка одинаковой длины:
# имена str,
# ставка int,
# премия str с указанием процентов вида «10.25%».
# Вернуть словарь с именем в качестве ключа и суммой
# премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии.

# Вариант 1.

# premium = 0.1025
#
# def create_list_rate():  # Создаем последовательность и помещаем в список
#     print('С клавиатуры введите список элементов(ставки), по окончанию ввода нажмите Enter')
#     new_list_rate = []
#     while True:
#         try:
#             element = float(input('> '))
#             float(element)
#             new_list_rate.append(element)
#         except:
#             break
#     return new_list_rate
#
# def create_list_name():  # Создаем последовательность и помещаем в список
#     print('С клавиатуры введите список элементов(имена), по окончанию ввода нажмите Enter')
#     new_list_name = []
#     while True:
#         try:
#             element = str(input('> '))
#             if element == '' or element == ' ':
#                 break
#             new_list_name.append(element)
#         except:
#             break
#     return new_list_name
#
# def create_list_dictionary_sum_premium(list_rate, list_name):
#     list_premium = []
#     for i in range(len(list_rate)):
#         list_premium.append(float("{0:.2f}".format(list_rate[i] * premium)))
#
#     list_dict_premium = dict(zip(list_name, list_premium))
#     return list_dict_premium
#
# def main():
#     new_list_rate = create_list_rate()
#     # print(new_list_rate)
#     new_list_name = create_list_name()
#     # print(new_list_name)
#     if (len(new_list_rate)) == 0 or (len(new_list_rate) == 0) \
#             or len(new_list_rate) != len(new_list_name):
#         print('Отсутствуют элементы в списке или кого-то не хватает')
#         exit()
#     list_dict_premium = create_list_dictionary_sum_premium(new_list_rate, new_list_name)
#     print(list_dict_premium)
#
# main()

# Вариант 2.

# def salary(names, rate, bonus):
#     workers ={}
#     for i in range (len(names)):
#         percent = float(bonus[i].replace('%',''))/100
#         workers[names[i]] = percent*rate[i] + rate[i]
#     return workers
#
# names = ['Петров','Иванов','Денисов','Сидоров']
# rate = [15000, 12500, 13700, 21000]
# bonus = ['9.25%', '10.25%', '15%', '11.10%']
# workerSalary = salary(names, rate, bonus)
# print(workerSalary)

# Задача №6

# Функция получает на вход список чисел и два индекса.
# Вернуть сумму чисел между между переданными индексами.
# Если индекс выходит за пределы списка, сумма считается
# до конца и/или начала списка.

# def indRange(ind, limit):
#     if ind < 0 : ind = 0
#     if ind > limit : ind = limit - 1
#     return ind
# def sumNums(myList, ind, ind2):
#     ind = indRange(ind, len(myList))
#     ind2 = indRange(ind2, len(myList))
#     sum = 0
#     for i in  range(ind, ind2+1):   #сумма включая числа под заданными инксами
#     #for i in range(ind+1, ind2):    # сумма без чисел под индексами
#         sum = sum + myList[i]
#     return sum
# myList = [1, 3, 5, 2, 4, 6, 8]
# ind = int(input('введите индекс №1 - >> '))
# ind2 = int(input('введите индекс №2 - >> '))
# print(sumNums(myList, ind, ind2))

# Задача №7

# Функция получает на вход словарь с названием компании в качестве ключа
# и списком с доходами и расходами (3-10 чисел) в качестве значения.
# Вычислите итоговую прибыль или убыток каждой компании.
# Если все компании прибыльные, верните истину, а если хотя бы одна убыточная — ложь.

# Вариант 1.

# list_company = ['New Company', 'Real Company', 'Company', 'CompBiz',
#                 'Mega brand', 'Mega King', 'Everything', 'Modest']
#
# list_profit_and_loss = [(100, 200, 300, -100, -200), (200, 600, 400, -300, -400),
#                         (200, 300, 300, -500, -100), (200, 200, 100, -100, -400),
#                         (100, 100, 100, -100, -100), (100, 300, 100, -100, -100),
#                         (300, 200, 100, -100, -200), (400, 600, 100, -100, -100)]
#
# list_dictionary = dict(zip(list_company, list_profit_and_loss))
# keys = list(list_dictionary.keys())
#
# def check_company():
#     for i in range(len(list_dictionary)):
#         if sum(list_dictionary[keys[i]]) < 0:
#             return False
#     return True
#
# print(check_company())

# Вариант 2.

# def positiveBalans(company):
#     for comp, balans in company.items():
#         if sum(balans) >= 0:
#             x = True
#         else:
#             x = False
#             break
#     return True if x == True else False
#
# company = {
#     'CompanyOne': [1000, 123331, 1000, 2000],
#     'CompanyTwo': [9999, -1000, 12000],
#     'CompanyThree': [10000, -23322, 100000, -9999]
# }
# print(positiveBalans(company))

# Задача №8

# Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
# Напишите функцию, которая при запуске заменяет содержимое переменных оканчивающихся
# на s (кроме переменной из одной буквы s) на None.
# Значения не удаляются, а помещаются в одноимённые переменные без s на конце.

# names = "Ivan"
# next = 6
# tigers = "White"
# dogs = "Rex"
# mute = 7
# ENDSWITH_STR = 's'
#
# def changing_variable_names():
#     glob = globals()
#     print(glob)
#     print()
#     for key in tuple(glob.keys()):
#         if key.endswith(ENDSWITH_STR):
#             temp = glob[key]
#             glob[key] = None
#             glob[key[: -1]] = temp
#     print(glob)
#
#
# changing_variable_names()
# print()
# print("check")
# print()
# print(names, name)
# print(tigers, tiger)
# print(dogs, dog)

# Вот такая конструкция еще используется, как точка входа:

# if __name__ == '__main__':
#     main(sys.argv)

# Задача с вещами и рюкзаком, но через рекурсию.

# Создайте словарь со списком вещей для похода в качестве
# ключа и их массой в качестве значения. Определите, какие
# вещи влезут в рюкзак, передав его максимальную
# грузоподъёмность. Достаточно вернуть один допустимый вариант.

# myDict = {'продукты': 10, 'котел': 2.1, 'хлеб': 0.7, 'топор': 2.3, 'динамит': 1, 'вода': 1.5, 'палатка': 2, 'арбуз': 8}
# listKeys = list(myDict.keys())
# listItems = list(myDict.values())
# print(type(listItems))
# maxWeight = 13
# someList=[]
# def func(someList, index, weight):
#     print('Уже уложено:', someList)
#     for i in range(index, len(listKeys)):
#         print('Пробуем положить', listKeys[i])
#         if listItems[i]+weight <= maxWeight :
#             emptyList = someList.copy()
#             emptyList.append(listKeys[i])
#             print('Влазит')
#             func(emptyList, i+1, weight+listItems[i])
#         else: print('Не влазит')
#     if len(someList) >= 3 : print(someList, weight)
# func(someList, 0, 0)

# Задача 1 ДЗ

# Напишите функцию для транспонирования матрицы.


# def transparent_matrix(*x_list: list[[int]]) -> list[()] | str:
#     is_transparent = True
#     col = len(x_list[0])
#     for a in list(x_list):
#         if len(a) != col:
#             is_transparent = False
#     if is_transparent:
#         return list(zip(*x_list))
#     else:
#         return 'Матрицу нельзя транспорировать'
#
#
# print(transparent_matrix([3, 5, 6], [2, 6, 2], [10, 0, 1]))

# Задача 2 ДЗ

# Напишите функцию, принимающую на вход только ключевые
# параметры и возвращающую словарь, где ключ — значение
# переданного аргумента, а значение — имя аргумента. Если
# ключ не хешируем, используйте его строковое представление.

# def hash_dicts(**kwargs):
#     reverse_dict = dict()
#     for key, value in kwargs.items():
#         if isinstance(value, (list, dict, set)):
#             value = str(value)
#         reverse_dict[value] = key
#     return reverse_dict
#
#
# print(hash_dicts(подруги=['Света', 'Лена'], друзья={1: "Костя", 2: "Петя"}))

# Задача 3 ДЗ

# Напишите программу банкомат.
# Начальная сумма равна нулю
# Допустимые действия: пополнить, снять, выйти
# Сумма пополнения и снятия кратны 50 у.е.
# Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# После каждой третей операции пополнения или снятия начисляются проценты - 3%
# Нельзя снять больше, чем на счёте.
# При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной.
# Любое действие выводит сумму денег.

# Возьмите задачу о банкомате из семинара 2. Разбейте её
# на отдельные операции — функции. Дополнительно сохраняйте
# все операции поступления и снятия средств в список.


from datetime import date

bank = 0
count = 0
percent_take = 0.015
percent_add = 0.03
percent_tax = 0.01

def add_bank(cash: float) -> None:
    global bank
    global count
    bank += cash
    count += 1
    if count % 3 == 0:
        bank = bank + percent_add * bank
        print("Начислены проценты в размере: ", percent_add * bank)

def take_bank(cash: float) -> None:
    global bank
    global count
    bank -= cash
    count += 1

    if cash * percent_take < 30:
        bank -= 30
        print("Списаны проценты за cash: ", 30)
    elif cash * percent_take > 600:
        bank -= 600
        print("Списаны проценты за cash: ", 600)
    else:
        bank -= cash * percent_take
        print("Списаны проценты за cash: ", cash * percent_take)
    if count % 3 == 0:
        bank = bank + percent_add * bank
        print("Начислены проценты в размере: ", percent_add * bank)


def exit_bank():
    print("Спасибо!\n")
    exit()

def check_bank() -> int:
    while True:
        cash = int(input("Введите сумму опреации кратную 50\n"))
        if cash % 50 == 0:
            return cash

list_operation = []

while True:
    action = input("Ввведите номер операции:\n1 - Снять деньги\n2 - Пополнить баланс\n3 - Баланс\n4 - Историю операций\n5 - Выход\n")

    if action == '1':
        if bank > 5_000_000:
            bank = bank - bank * percent_tax
            print("Списан налог на богатство: ", bank * percent_tax)
        cash = check_bank()
        if cash < bank:
            take_bank(cash)

            list_operation.append([str(date.today()), -1 * cash])
        else:
            print("no money\n")
        if bank > 5_000_000:
            bank = bank - bank * percent_tax
            print("Списан налог на богатство: ", bank * percent_tax)
        print("Баланс = ", bank)
    elif action == '2':
        cash = check_bank()
        add_bank(cash)
        if bank > 5_000_000:
            bank = bank - bank * percent_tax
            print("Списан налог на богатство: ", bank * percent_tax)
        print("Баланс = ", bank)

        list_operation.append([str(date.today()), cash])

    elif action == '3':
        print("Баланс = ", bank)
    elif action == '4':
        print(list_operation)
    else:
        exit_bank()