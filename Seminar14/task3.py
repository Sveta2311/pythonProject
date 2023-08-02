# Задача 3

# Напишите для задачи 1 тесты unittest. Проверьте следующие варианты:
# возврат строки без изменений,
# возврат строки с преобразованием регистра без потери символов,
# возврат строки с удалением знаков пунктуации,
# возврат строки с удалением букв других алфавитов,
# возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1).

import task1_2 as test
import unittest

print(test.testStringOne("He44o"))

class userClass(unittest.TestCase):
    def testStr(self):
        text = "abyrvalg"
        self.assertEqual(text, test.testStringOne(text))

    def testStrRegistr(self):
        text = "DDff"
        #self.assertEqual(text, test.testStringOne(text))
        self.assertEqual(text.lower(),test.testStringOne(text))

    def testStrDelPoints(self):
        text = "ff,;:ss"
        #self.assertEqual(text,test.testStringOne(text))
        self.assertEqual("ffss", test.testStringOne(text))

    def testStrSymbols(self):
        text="абыр ппп"
        #self.assertEqual(text,test.testStringOne(text))
        self.assertEqual(" ", test.testStringOne(text))

    def testAll(self):
        text ="ЫЫ ss, Y"
        #self.assertEqual(text, test.testStringOne(text))
        self.assertEqual(" ss y", test.testStringOne(text))

if __name__=="__main__":
    unittest.main(verbosity=2)
