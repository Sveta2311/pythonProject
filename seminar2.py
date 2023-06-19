# a = 42
# b = 4.5
# c = 'sveta'
# d = []
# print(type(a), type(b), type(c), type(d))
# Создайте в переменной data список значений разных типов перечислив их через запятую внутри квадратных скобок. Для каждого элемента в цикле выведите:
# порядковый номер начиная с единицы
# значение
# адрес в памяти (id)
# размер в памяти (sys.getsizeof(list[i]))
# хэш объекта (hash)
# результат проверки на целое число только если он положительный
# результат проверки на строку только если он положительный
# Добавьте в список повторяющиеся элементы и сравните на результаты.
# import sys
# data = [42, 4.5, 'sveta', 42, 4.5, 'sveta']
# for i in range(0, 6):
#  print(i+1, data[i], id(i), sys.getsizeof(data[i]), hash(data[i]), 'celoe' if isinstance(data[i], int) else '', \
#        'stroka' if isinstance(data[i], str) else '')
# Напишите программу, которая получает целое число и возвращает
# его двоичное, восьмеричное строковое представление.
# Функции bin и oct используйте для проверки своего
# результата, а не для решения.
# Дополнительно:
# Попробуйте избежать дублирования кода
# в преобразованиях к разным системам счисления
# Избегайте магических чисел
# Добавьте аннотацию типов где это возможно

# def conv_Number(num_Dec, ss):
#     digits = "0123456789ABCDEFGHI"          # Задаем символы для разных СС
#     num_Conv = ""                           # Создаем переменную для конечного результата
#     while (num_Dec > 0):        # Запускаем цикл для отделения остатков от деления и запись их в строку
#         k = num_Dec % ss                    # Получаем остаток от деления
#         num_Conv = digits[k] + num_Conv     # Записываем получившийся остаток в конечную строку
#         num_Dec = num_Dec // ss             # Делим без остатка
#     return num_Conv
#
# def Main():
#     number = int(input('Число в десятичной СС: '))
#     for i in range(2, 17):
#         print(f'Ответ в {i}-ой СС = ', conv_Number(number, i))
#
# Main()
# Напишите программу, которая вычисляет площадь
# круга и длину окружности по введённому диаметру.
# Диаметр не превышает 1000 у.е.
# Точность вычислений должна составлять
# не менее 42 знаков после запятой.
# import math
# import decimal
# decimal.getcontext().prec = 50
# # from decimal import Decimal
# # myPi = Decimal(math.pi)
# # diam = Decimal(input('введите диаметр : '))
# # print(f'Длина окружности = {myPi*(diam)}, Площадь круга {myPi*(diam/2 * diam/2)} ')
# from decimal import *
# import math as M
#
# def square_Сircle (diametr):
#     sq_Сircle = Decimal(M.pi * ((diametr/2) ** 2))
#     return sq_Сircle
#
# def length_Сircle (diametr):
#     len_Сircle = Decimal(M.pi * diametr)
#     return len_Сircle
#
# def Main():
#     diametr = float(input('Введите диаметр круга - '))
#     if diametr <= 1000:
#         print('Площадь круга = ', square_Сircle(diametr))
#         print('Длина круга = ', length_Сircle(diametr))
#     else:
#         print('Диаметр не должен превышать 1000 у.е.')
#
# Main()
# Напишите программу, которая решает квадратные уравнения даже если
# дискриминант отрицательный.
# Используйте комплексные числа
# для извлечения квадратного корня.

# import math
# import cmath
#
# def quadratic_equation(a, b, c):
#     discr = b ** 2 - 4 * a * c
#     print("Дискриминант D = %.3f" % discr)
#
#     if discr > 0:
#         x1 = (-b + math.sqrt(discr)) / (2 * a)
#         x2 = (-b - math.sqrt(discr)) / (2 * a)
#         print("x1 = %.3f \nx2 = %.3f" % (x1, x2))
#     elif discr == 0:
#         x = -b / (2 * a)
#         print("x = %.3f" % x)
#     elif discr < 0:
#         x1 = complex((-b + cmath.sqrt(discr)) / (2 * a))
#         x2 = complex((-b - cmath.sqrt(discr)) / (2 * a))
#         print(f'x1 = {x1} \nx2 = {x2}')
#
# def Main():
#     print("Введите коэффициенты для уравнения")
#     print("ax^2 + bx + c = 0:")
#     a = float(input("a = "))
#     b = float(input("b = "))
#     c = float(input("c = "))
#     quadratic_equation(a, b, c)
#
# Main()
# Напишите программу банкомат.
# Начальная сумма равна нулю
# Допустимые действия: пополнить, снять, выйти
# Сумма пополнения и снятия кратны 50 у.е.
# Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# После каждой третей операции пополнения или снятия начисляются проценты - 3%
# Нельзя снять больше, чем на счёте
# При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
# Любое действие выводит сумму денег
# def invoice(money):
#     print(f'На счету {round(money, 2)} y.e.')
# def menuAtm():
#     print('--'*20)
#     print(f'Вывести сумму на счете, нажмите : 1')
#     print(f'Снять со счета, нажмите : 2')
#     print(f'Положить на счет, нажмите : 3')
#     print('--' * 20)
#     print(f'Для выхода нажмите 0')
#     print('--' * 20)
# def invoiceOut(money):
#     invoice(money)
#     while True:
#         print(f'Сколько хотите снять со счета? ')
#         outMoney = float(input(' ->> '))
#         if outMoney > money :
#             print(f'{invoice(money)}, введите сумму корректно')
#             continue
#         if bankTaxMax > outMoney - outMoney/bankTax > bankTaxMin : outMoney = outMoney - outMoney/bankTax
#         elif bankTaxMin > outMoney - outMoney/bankTax : outMoney = outMoney - bankTaxMin # Тут снимаем минимальную таксу, не со счета потому что на счете может не быть суммы для банка
#         else : outMoney = outMoney - bankTaxMax
#         if money > rich :
#             money = money - money/tax - outMoney
#             break
#         else :
#             money = money - outMoney
#             break
#     return money
# def invoiceIn(money):
#     while True :
#         print(f'Сколько хотите положить? (кратно 50)')
#         moneyIn = int(input(' ->> '))
#         if moneyIn%50 != 0 :
#             print(f'Введите сумму кратную 50 ')
#             continue
#         elif moneyIn % 50 == 0 :
#             money = money + moneyIn
#             break
#     return money
#
# # constants
# money = 0
# bankTax = 1.015
# bankTaxMin = 30
# bankTaxMax = 600
# bankPercent = 1.03
# rich = 5000000
# tax = 1.1
# # программа
# opCount = 1 # первая операция
# while True:
#     menuAtm()
#     if opCount % 3 == 0 : money = money * bankPercent
#     button = input(' ->> ')
#     if button == '1' : invoice(money)
#     elif button == '2' : money = invoiceOut(money)
#     elif button == '3' : money = invoiceIn(money)
#     elif button == '0' : break
#     else: print(f'Непонятно чего там нажали, повторите ')
#     opCount +=1

# constant.py

# zero = 0
# one = 1
# two = 2
# three = 3
# four = 4
# five = 5
# six = 6
# seven = 7
# eight = 8
# nine = 9
#
# licevoi_chet_10001 = 0
# count_10001 = 0
# operation_counter = 3
# percent_count = 0.03
# perсent_min = 30
# perсent_avg = 0.015
# perсent_max = 600
# perсent_luxury_tax = 0.1
# line_luxury = 5_000_000
# import base_of_clients
#
# import time
# from os import system
#
# def find_Index(id_client):              # Поиск индекса по ID
#     index = 0
#     index2 = 0
#     for i in base_of_clients.id_clients:
#         try:
#             index2 = i.index(id_client)
#         except ValueError:
#             index2 = -1
#         if index2 != -1:
#             break
#         index += 1
#     if index2 == -1:
#         print("Нет такого ID")
#         time.sleep(2)
#         system("cls")
#         Main()
#     else:
#         return index
#
# def choice_Method(index):            # Выбор метода
#     balance(index)
#     print('1. Пополнить \n 2. Снять \n 3. Выйти')
#     method = int(input('Выберите пункт: '))
#     if method == 1:
#         luxury_Tax(index)
#         top_Up(index)
#     elif method == 2:
#         check_Balance(index)
#         luxury_Tax(index)
#         take_Off(index)
#     elif method == 3:
#         print('Досвидания!')
#         exit()
#     else:
#         choice_Method(index)
#
# def count_Client(money, index):        # Счетчик на операции
#     if base_of_clients.id_clients[index][2] < operation_counter:
#         base_of_clients.id_clients[index][2] = base_of_clients.id_clients[index][2] + 1
#         return
#     elif base_of_clients.id_clients[index][2] == operation_counter:
#         base_of_clients.id_clients[index][2] = 0
#         base_of_clients.id_clients[index][1] = base_of_clients.id_clients[index][1] + \
#                                                money * percent_count
#         print(f'Начислен кэшбэк в размере {100 * percent_count} %')
#         balance(index)
#         return
#
# def luxury_Tax(index):               # Налог на роскошь
#     if base_of_clients.id_clients[index][1] <= line_luxury:
#         return
#     elif base_of_clients.id_clients[index][1] > line_luxury:
#         base_of_clients.id_clients[index][1] = base_of_clients.id_clients[index][1] - \
#                                                base_of_clients.id_clients[index][1] * perсent_luxury_tax
#         print(f'Изъят налог на роскошь в размере - {100 * perсent_luxury_tax} %')
#         balance(index)
#         return
#
# def check_Balance(index):            # Проверка баланса
#     if base_of_clients.id_clients[index][1] <= 0:
#         print("На вашем счет недостаточно средств для снятия наличных")
#         time.sleep(2)
#         system("cls")
#         choice_Method(index)
#     else:
#         return
#
#
# def balance(index):                  # Вывод баланса
#     print(f'Ваш баланс: {base_of_clients.id_clients[index][1]} у.е. \n')
#     time.sleep(2)
#     system("cls")
#     return
#
# def top_Up(index):                   # Внесение наличных
#     money = int(input('Внесите купюры кратные 50 у.е.: '))
#     if money % 50 == 0 and money > 0:
#         base_of_clients.id_clients[index][1] = base_of_clients.id_clients[index][1] + money
#         count_Client(money, index)
#         choice_Method(index)
#     else:
#         balance(index)
#         top_Up(index)
#
# def take_Off(index):                 # Снятие наличных
#     money = int(input('Укажите сумму, которую хотите снять: '))
#     if (money > 0):
#         if ((money + money * perсent_min) <= perсent_min) \
#                 and ((money + perсent_min) <= base_of_clients.id_clients[index][1]):
#             base_of_clients.id_clients[index][1] = base_of_clients.id_clients[index][1] - \
#                                                    (money + perсent_min)
#             count_Client(money, index)
#             choice_Method(index)
#         elif ((money + money * perсent_min) >= perсent_max) \
#                 and ((money + perсent_max) <= base_of_clients.id_clients[index][1]):
#             base_of_clients.id_clients[index][1] = base_of_clients.id_clients[index][1] - \
#                                                    (money + perсent_max)
#             count_Client(money, index)
#             choice_Method(index)
#         elif ((money * perсent_min) < perсent_max) \
#                 and ((money + money * perсent_min) <= base_of_clients.id_clients[index][1]):
#             base_of_clients.id_clients[index][1] = base_of_clients.id_clients[index][1] - \
#                                                    (money + money * perсent_min)
#             count_Client(money, index)
#             choice_Method(index)
#         else:
#             print('Данная сумма не доступна для снятия')
#             balance(index)
#             take_Off(index)
#     else:
#         print('Вы указали некорректную сумму')
#         balance(index)
#         choice_Method(index)
#
# def Main():                     # Приветствие
#     print("Добро пожаловать в сборкомат")
#     id_client = int(input('Укажите свой ID: '))
#     index = find_Index(id_client)
#     choice_Method(index)
#
# Main()

# Напишите программу, которая принимает две строки
# вида “a/b” — дробь с числителем и знаменателем.
# Программа должна возвращать сумму
# и *произведение дробей. Для проверки своего
# кода используйте модуль fractions.
# import math
#
# def sum_Fraction(number_frac_1, number_frac_2):     # Сложение дробей и приведение к НОД
#     sum_frac = [int(number_frac_1[0]) * int(number_frac_2[1]) \
#                        + int(number_frac_2[0]) * int(number_frac_1[1]),
#                 int(number_frac_1[1]) * int(number_frac_2[1])]
#     nod = math.gcd(sum_frac[0], sum_frac[1]) #Наименьший общий делитель
#     sum_frac = [int(sum_frac[0] / nod), int(sum_frac[1] / nod)]
#     print('Cумма дробей = ', sum_frac[0], '/', sum_frac[1])
#
# def mult_Fraction(number_frac_1, number_frac_2):    # Умножение дробей и приведение к НОД
#     mult_frac = [int(number_frac_1[0]) * int(number_frac_2[0]),
#                  int(number_frac_1[1]) * int(number_frac_2[1])]
#     nod = math.gcd(mult_frac[0], mult_frac[1])
#     mult_frac = [int(mult_frac[0] / nod), int(mult_frac[1] / nod)]
#     print('Произведение дробей = ', mult_frac[0], '/', mult_frac[1])
#
# def Main():
#     number_frac_1 = str(input('Введите первое число вида a/b - ')).split('/')
#     number_frac_2 = str(input('Введите второе число вида a/b - ')).split('/')
#     sum_Fraction(number_frac_1, number_frac_2)
#     mult_Fraction(number_frac_1, number_frac_2)
#
# Main()

import fractions
# задача с дробями
str1 = str(input('Введите дробь вида 3/4 : '))
str2 = str(input('Еще одну : '))
first = str1.split('/')
second = str2.split('/')
summa = str(int(first[0]) * int(second[1]) + int(first[1]) * int(second[0])) + '/' + str(int(second[1]) * int(first[1]))
mult = str( int(first[0]) * int( second[0])) + '/' + str ( int(first[1]) * int(second[1]))
print(f'Сумма {summa}, Произведение {mult}')
f1 = fractions.Fraction(int(first[0]), int(first[1]))
f2 = fractions.Fraction(int(second[0]), int(second[1]))
print(f'Проверка Fractions сумма {f1+f2}, произведение {f1*f2}')