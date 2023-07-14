# Задача 9

# Соберите из созданных на уроке и в рамках домашнего задания функций
# пакет для работы с файлами разных форматов.


from task8 import get_dirs_json, write_json, write_csv, write_pickle

if __name__ == '__main__':
    dict_json = get_dirs_json('.')
    write_json('dir_info_from_pack.json', dict_json)
    write_csv('dir_info_from_pack.csv', dict_json)
    write_pickle('dir_info_from_pack.pickle', dict_json)
