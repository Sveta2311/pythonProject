# Задача 1

# Создайте класс-функцию, который считает факториал числа при вызове экземпляра.
# Экземпляр должен запоминать последние k значений.
# Параметр k передаётся при создании экземпляра.
# Добавьте метод для просмотра ранее вызываемых значений и их факториалов.

# Задача 2

# Доработаем задачу 1.
# Создайте менеджер контекста, который при выходе
# сохраняет значения в JSON файл.

# import json
#
#
# class Factorial:
#     def __init__(self, k):
#         self.k = k
#         self.start = 1
#         self.dictn = {self.start: 1}
#
#     def __call__(self, n, *args, **kwargs):
#         self.start = 1
#         for i in range(1, n + 1):
#             self.start *= i
#             self.dictn[i] = self.start
#             if len(self.dictn) >= self.k:
#                 self.dictn.pop(i - self.k, 0)
#         return self.start
#
#     def __str__(self):
#         return f'{self.dictn}'
#
#     def __enter__(self):
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         # dict2 = {}
#         # for _ in self.dictn:
#         #     dict2.update(self.dictn.items())
#         with open("new_json.json", "w", encoding="utf-8") as file:
#             json.dump(self.dictn, file, indent=2)
#         print("Завершено")
#
#
# with Factorial(5) as f:
#     print(f(10))
#
#
# print(f)

# Задача 3

# Создайте класс-генератор.
# Экземпляр класса должен генерировать факториал числа в
# диапазоне от start до stop с шагом step.
# Если переданы два параметра, считаем step=1.
# Если передан один параметр, также считаем start=1.

# class Factorial_gen:
#     def __init__(self, stop, start=1, step=1):
#         self.start = start
#         self.stop = stop
#         self.step = step
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.start < self.stop:
#             self.start += self.step
#             p = Factorial(5)
#             print(self.start)
#             return p(self.start)
#         else:
#             raise StopIteration
#
# if __name__ == '__main__':
#     chars = Factorial_gen(10, 2, 2)
#     for c in chars:
#         print(c)

# Задача 4

# Доработайте класс прямоугольник из прошлых семинаров.
# Добавьте возможность изменять длину и ширину прямоугольника и встройте контроль недопустимых значений (отрицательных).
# Используйте декораторы свойств.

# Задача 5

# Доработаем прямоугольник и добавим экономию памяти для хранения свойств экземпляра без словаря __dict__.

# class rectangle():
#     __slots__ = ('_a', '_b')
#
#     def __init__(self, a, b):
#         self._a = a
#         self._b = b
#
#
#     @property
#     def side1(self):
#         return self._a
#
#     @property
#     def side2(self):
#         return self._b
#
#     @side1.setter
#     def side1(self, value):
#         if value > self.min:
#             self._a = value
#         else:
#             raise ValueError(f'Значение должно быть больше 0: {self._a}')
#
#     @side2.setter
#     def side2(self, value):
#         if value > self.min:
#             self._b = value
#         else:
#             raise ValueError(f'Значение должно быть больше 0: {self._b}')
#
#
# pr1 = rectangle(2, 4)
# pr2 = rectangle(4, 2)
# print(pr1.side1)
# print(pr1.side2)
# pr1.side1 = 5
# print(pr1.side1)
# pr1.side2 = 10
# print(pr1.side2)

# Задача 6

# Изменяем класс прямоугольника.
# Заменяем пару декораторов проверяющих длину и ширину на дескриптор с валидацией размера.

class Range:

    def __init__(self, min_value: int = None, max_value: int = None):

        self.min_value = min_value

        self.max_value = max_value


    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):

        return getattr(instance, self.param_name)

    def __set__(self, instance, value):

        self.validate(value)
        setattr(instance, self.param_name, value)

    def validate(self, value):
        print(self.min_value)

        if not isinstance(value, int):
            raise TypeError(f'Значение {value} должно быть целым числом')
        if self.min_value is not None and value < self.min_value:
            raise ValueError(f'Значение {value} должно быть больше или равно {self.min_value}')
        if self.max_value is not None and value >= self.max_value:
            raise ValueError(f'Значение {value} должно быть меньше {self.max_value}')


class rectangle():
    a = Range(1, 50)
    b = Range(2, 40)

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __repr__(self):
        return f'{self.a} {self.b}'


if __name__ == '__main__':
    pr1 = rectangle(2, 4)
    pr2 = rectangle(60, 10)
    print(f'{pr1 = }')
    print(f'{pr2 = }')
    print(type(pr1.a))
