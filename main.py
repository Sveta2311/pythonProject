# vis_year_mult_four_h = 400     # год, номер которого кратен 400, — високосный
# vis_year_mult_one_h = 100     # остальные года, номер которых кратен 100, — невисокосные;
# vis_year_mult_four = 4         # остальные года, номер которых кратен 4, — високосные;
#
# low_line = 1
# high_line = 999
# len_three = 3
# len_two = 2
# num_dec = 10
# square = 2
#
# zero = 0
#
# def check_year(y):
#     if (y % vis_year_mult_four == zero) \
#             and (y % vis_year_mult_one_h != zero) \
#             or (y % vis_year_mult_four_h == zero):
#         return "Данный год является високостный"
#     else:
#         return "Данный год не является високостным"
#
# def Main():
#     year = float(input('Введите год - '))
#     print(check_year(year))
#
# Main()
# A = 1
# B = 10
# C = 100
# minDig = 1
# maxDig = 999
# while True:
#     n = int(input('введите число от 1 до 999 : '))
#     if minDig <= n <= maxDig: break
# if n // A < B : x = n * n
# elif n // B < B : x = (n % B) * (n//B)
# elif n // C < B : x = (n % B) * C + (((n % C) // B) * B) + (n // C)
# print(n,' : ',x)
# x =int(input ("введите число : "))
# for i in range(0, x) :
#     print (' '* (x-i) + '*' * (i) + '*' * (i+1))
print('Таблица умножения')

# for i in range(2, 10):
#     for k in range(2, 6):
#         print(f'{k} * {i} = {i * k}\t', end='')
#     print('')
# print('')
# for i in range(2, 10):
#     for k in range(6, 10):
#         print(f'{k} * {i} = {i * k}\t', end='')
#     print('')
# def triangle(a,b,c):
#     if (a == b) and (b == c):
#         return 'Треугольник равносторонний'
#     elif ((a == b) or (a == c) or (b == c)) and (a + b > c) and (a + c > b) and (b + c > a):
#         return 'Треугольник равнобедренный'
#     elif (a + b > c) and (a + c > b) and (b + c > a):
#         return 'Треугольник существует'
#     else:
#         return 'Треугольник не существует'
#
# def Main():
#     print("Введите стороны треугольника a, b, c")
#     a = float(input("a = "))
#     b = float(input("b = "))
#     c = float(input("c = "))
#     print(triangle(a,b,c))
#
# Main()
# prime = True
# maxDig = 100000
# while True:
#     n = int(input('введите число от 1 до 100000. n = '))
#     if 0 < n < maxDig: break
# for i in range (2, n//2):
#     if n%i == 0 :
#         prime = False
#         break
# if prime : print('число ', n, ' простое')
# else : print('число ', n, ' составное')
from random import randint
num = randint(0, 10)
count = 1
while count < 10:
    n = int(input('число :'))
    if n == num :
        print('угадал')
        break
    elif n > num : print('мое число меньше. ', count+1, ' попытка')
    else : print('мое число больше ',count+1, ' попытка')
    count +=1
print('мое число : ', num)