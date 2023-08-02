# Задача 5

# На семинарах по ООП был создан класс прямоугольник,
# хранящий длину и ширину, а также вычисляющую периметр,
# площадь и позволяющий складывать и вычитать
# прямоугольники, беря за основу периметр.
# Напишите 3-7 тестов unittest для данного класса.

import unittest


class Rectangle():
    def verifyRectangle(self, width, lenght):
        if width <= 0 or lenght <= 0 :
            print('сторона меньше или равна 0')
            return False
        else: return True

    def __init__ (self, lenght: int, width: int):
        if self.verifyRectangle(lenght, width):
            self.lenght = lenght
            self.width = width
        else : print('объект не создан')


    def __str__(self):
        text = str(self.width) + " " + str(self.lenght)
        return text

    def __eq__(self, other):
        if (self.width == other.width and self.lenght == other.lenght) or (self.width == other.lenght and self.lenght == other.width):
            return True
        else : return False

class userClass(unittest.TestCase):
    _rectangle = Rectangle(3, 6)

    def testOne(self):
        self.assertEqual(self._rectangle, self._rectangle)
        #self.assertEqual(self._rectangle, Rectangle(4,5))     # Failed
        self.assertEqual(self._rectangle, Rectangle(3, 6))
        self.assertEqual(self._rectangle, Rectangle(6, 3))


if __name__=="__main__":
    r1 = Rectangle(3,5)
    print(r1)
    unittest.main()