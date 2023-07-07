# Напишите функцию группового переименования файлов. Она должна:
# принимать параметр желаемое конечное имя файлов.
# При переименовании в конце имени добавляется порядковый номер.
# принимать параметр количество цифр в порядковом номере.
# принимать параметр расширение исходного файла.
# Переименование должно работать только для этих файлов внутри каталога.
# принимать параметр расширение конечного файла.
# принимать диапазон сохраняемого оригинального имени.
# Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
# К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.

import os


# 1 - новое имя, 2 - количество цифр в порядковом номере, 3 - выбор элементов по расширению
# 4 - изменить на заданное расширение, 5 - диапазон символов от старого имени файла.

def renames(new_name: str, numbers: int = 1, select_expansion: str = '',
            end_expansion: str = '', range_char_old_name: list = []):
    # создаём спиок файлов в текущей дериктории
    all_files_directory = os.listdir()

    if len(str(len(all_files_directory))) > numbers:
        numbers = len(str(len(all_files_directory)))

    start_count_number = 1

    # генерируем строку из '0', длиной numbers
    file_number = ''
    while numbers:
        file_number += '0'
        numbers -= 1

    # проходимся по каждому файлу в текущей директории
    for file in all_files_directory:
        if file == "HW7.py":
            continue
        if len(file.split('.')) <= 1:
            continue
        # создаём две переменные (количество символов старого имени, расширение старого имени)
        count_char_old_name, expansion_old_file = '', file.split('.')[1]
        # если при указании аргументов задали выбранное расширени и такого нет в списке файлов, то пропускаем итерацию
        if select_expansion != '' and expansion_old_file != select_expansion:
            continue
        # если не указывали аргумент изменения расширения, то оставвляем прежнее расширение
        if end_expansion == '':
            end_expansion = expansion_old_file
        file_number = file_number[:-len(str(start_count_number))] + str(start_count_number)
        # если в аргументах указали с какого по какой символ нужно сохранить от старого имени, то формируем срез
        if len(range_char_old_name) == 2:
            count_char_old_name = file[range_char_old_name[0] - 1:range_char_old_name[1]:]
        # вызываем метод переименования файла для склейки получившегося имени
        os.rename(file, f'{count_char_old_name}{new_name}{file_number}.{end_expansion}')

        start_count_number += 1


renames('new_name', 5, 'txt', 'csv', [1, 4])
