# Задача 2

# Напишите функцию, которая в бесконечном цикле запрашивает имя,
# личный идентификатор и уровень доступа (от 1 до 7).
# После каждого ввода добавляйте новую информацию в JSON файл.
# Пользователи группируются по уровню доступа.
# Идентификатор пользователя выступает ключём для имени.
# Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
# При перезапуске функции уже записанные в файл данные должны сохраняться.

import json


def getAccessLevel():
    accessLevels = ['1', '2', '3', '4', '5', '6', '7']
    myDict = {}
    with open('access_file.json', 'a', encoding='utf-8') as read_access:
        try:
            myDict = json.load(read_access)
        except:
            pass
        read_access.close()
        while True:
            ident = input("введите личный идентификатор: ")
            if ident in myDict.keys():
                print("идентификатор уже используется")
            else:
                name = input("введите имя: ")
                while True:
                    access = input(f"введите уровень доступа с {min(accessLevels)} по {max(accessLevels)} : ")
                    if access not in accessLevels:
                        print("некорректный ввод")
                    else:
                        myDict[ident] = [name, access]
                        sortedDict = dict(sorted(myDict.items(), key=lambda item: item[1], reverse=True))
                        print(sortedDict)
                        with open('access_file.json', 'w', encoding="utf-8") as write_access:
                            new_entry = json.dumps(sortedDict, indent=2, separators=(',', ':'))
                            write_access.write(new_entry)
                            write_access.close()
                            break
                break


getAccessLevel()
