# Задача 4

# Создайте модуль с функцией внутри.
# Функция получает на вход загадку, список с возможными вариантами отгадок и количество попыток на угадывание.
# Программа возвращает номер попытки, с которой была отгадана загадка или ноль, если попытки исчерпаны.


# from seminar6 import zagadka
#
#
# if __name__ == '__main__':
#     print(zagadka('Висит груша, нельзя скушать?', ['лампочка', 'лампа', 'лампомпулечка'], 3))

# Задача 5

# Добавьте в модуль с загадками функцию, которая хранит словарь списков.
# Ключ словаря - загадка, значение - список с отгадками.
# Функция в цикле вызывает загадывающую функцию, чтобы передать ей все свои загадки.

# from seminar6 import archiv
#
#
# if __name__ == '__main__':
#      print(archiv())

# Задача 6

# Добавьте в модуль с загадками функцию, которая принимает на вход строку (текст загадки) и число (номер попытки, с которой она угадана).
# Функция формирует словарь с информацией о результатах отгадывания.
# Для хранения используйте защищённый словарь уровня модуля.
# Отдельно напишите функцию, которая выводит результаты угадывания из защищённого словаря в удобном для чтения виде.
# Для формирования результатов используйте генераторное выражение.

# from seminar6 import logAnswers, printDict
# import random
#
# if __name__ == '__main__':
#     logAnswers('Зимой и летом одним цветом', random.randint(3, 6))
#     logAnswers('Висит груша - нельзя скушать', random.randint(3, 6))
#     printDict()
