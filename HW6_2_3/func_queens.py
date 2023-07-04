from random import randint

import queens_true
import intersections
import random_queens

diagonals = intersections.diagonals
widths = intersections.wigths
queens = queens_true.queens
queens_arrangements = None


# вывод шахмотной доски с ферзями в терминал
def print_queens(queens):
    row_length = [[1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8]]
    squea = '[ ]'
    queen = ' ♛  '
    for i in range(0, 9):
        if i == 0:
            print("", end='')
        else:
            print(f'     {i}', '\t', end='')
    print('\n')

    for row in row_length[0]:
        for length in row_length[1]:
            if length == 1:
                print(row, '\t', end='')
            if row == queens[0][0] and length == queens[0][1]:
                print(queen, '\t', end='')
            elif row == queens[1][0] and length == queens[1][1]:
                print(queen, '\t', end='')
            elif row == queens[2][0] and length == queens[2][1]:
                print(queen, '\t', end='')
            elif row == queens[3][0] and length == queens[3][1]:
                print(queen, '\t', end='')
            elif row == queens[4][0] and length == queens[4][1]:
                print(queen, '\t', end='')
            elif row == queens[5][0] and length == queens[5][1]:
                print(queen, '\t', end='')
            elif row == queens[6][0] and length == queens[6][1]:
                print(queen, '\t', end='')
            elif row == queens[7][0] and length == queens[7][1]:
                print(queen, '\t', end='')
            else:
                print(squea, '\t', end='')
        print('\n')


# поиск пересечений ферзей на шахматной доске
def intersection_search(queens):
    count = 0

    for diagonal in diagonals:
        for coordinates_d in diagonal:
            for coordinates_q in queens:
                if coordinates_d == coordinates_q:
                    count += 1
        if count > 1:
            break
        count = 0

    for width in widths:
        for coordinates_c in width:
            for coordinates_d in queens:
                if coordinates_d == coordinates_c:
                    count += 1
        if count > 1:
            break
        count = 0

    print_queens(queens)

    if count > 1:
        print("В данной расстановке, ферзи пересекаются!")
        return False
    else:
        print('Задание выполнено, \nВсе ферзи раставлены согласно условию!')
        global queens_arrangements
        queens_arrangements = queens
        return True


# поиск четырёх правильных расположений ферзей с записью в файл .txt
def func_search_four_arrangements():
    global queens_arrangements
    count = 0
    arrangements_queen = open('true_placement_queens.txt', 'a')
    arrangements_queen.write('Список координат ферзей с правильной расстановкой:\n')
    while count < 4:
        rand = intersection_search(random_queens.queens_rnd_x_y())
        if rand == 0:
            continue
        count += 1
        arrangements_queen.write(f'{count} Координаты правильной расстановки - {queens_arrangements}\n')
    arrangements_queen.close()
    # with open('true_placement_queens.txt', 'a') as arrangements_queen:
    #     arrangements_queen.write(f'{count} Координаты правильной расстановки - {queens_arrangements}\n')
    # arrangements_queen = open('true_placement_queens.txt', 'r')
    # print(arrangements_queen.read())
    # arrangements_queen.close()