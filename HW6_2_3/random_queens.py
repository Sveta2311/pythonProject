from random import randint


# функция для рандомной расстановки ферзей по всему полю
def queens_rnd():
    queens = []
    for _ in range(1, 9):
        queens.append([randint(1, 8), randint(1, 8)])
    return queens


# функция для поиска правильной расстанвки ферзей
# с помощью рандома
def queens_rnd_x_y():
    queens = []
    count = 1
    for _ in range(1, 9):
        queens.append([count, randint(1, 8)])
        count += 1
    return queens


if __name__ == '__main__':
    print(queens_rnd())
    print(queens_rnd_x_y())