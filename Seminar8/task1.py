# Задача 1

# Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
# текстовый файл с псевдо именами и произведением чисел.
# Напишите функцию, которая создаёт из созданного ранее
# файла новый с данными в формате JSON.
# Имена пишите с большой буквы.
# Каждую пару сохраняйте с новой строки.

import json


def toJson():
    myDict = {}
    with open("unititled.txt", "r", encoding="utf-8") as nn:
        while res := nn.readline():
            myList = res.replace("\n", "").upper().split(', ')[0].split(' | ')
            myDict[myList[0]] = myList[1]
        nn.close()
    print(myDict)
    with open('new_user.json', 'w', encoding="utf-8") as f:
        result = json.dumps(myDict, indent=2, separators=(',', ':'), sort_keys=True)
        f.write(result)
        f.close()


toJson()
