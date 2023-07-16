# Задача 2

# Соберите пакет с играми из тех файлов, что уже были созданы в рамках курса.


from task import guess_function
from seminar2 import find_Index,choice_Method
if __name__ == '__main__':
    game1 = guess_function(7, 5)
    print(game1())

    print("Добро пожаловать в сборкомат")
    id_client = int(input('Укажите свой ID: '))
    index = find_Index(id_client)
    choice_Method(index)


