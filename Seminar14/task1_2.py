# Задача 1

# Создайте функцию, которая удаляет из текста все символы,
# кроме букв латинского алфавита и пробелов.
# Возвращается строка в нижнем регистре.

# Задача 2

# Напишите для задачи 1 тесты doctest. Проверьте следующие варианты:
# возврат строки без изменений,
# возврат строки с преобразованием регистра без потери символов,
# возврат строки с удалением знаков пунктуации,
# возврат строки с удалением букв других алфавитов,
# возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1).

import doctest

def testStringOne(text :str):
    """
    >>> testStringOne("sajkbdd___+++aslhdajsd;lj JHGHGJG al wqkjqwheh jksahdkjk")
    'sajkbddaslhdajsdlj jhghgjg al wkjwheh jksahdkjk'
    >>> testStringOne("567fgh")
    'fgh'
    """
    text = text.lower()
    myStr = "abcdefghijklmnoprstuvwxyz ".lower()
    textResult =""
    for i in text:
        if i in myStr:
            textResult = textResult+i
    return textResult

if __name__=="__main__":
    doctest.testmod(verbose=True)
    testStringOne("555lsjdjlaj")