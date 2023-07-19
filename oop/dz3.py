'''требуется проверить, возможно ли из представленных отрезков условной длины сформировать треугольник.
Для этого нужно создать класс TriangleChecker, принимающий только положительные числа.
С помощью метода is_triangle() возвращаются следующие значения (в зависимости от ситуации):
– можно построить треугольник;
– С отрицательными числами ничего не выйдет;
– Нужно вводить только числа;
– Невозможно создать треугольник с такими сторонами.
'''


class TriangleChecker:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        if type(self.a) is not int or type(self.b) is not int or type(self.c) is not int:
            print('Нужно вводить только числа')
        elif self.a < 0 or self.b < 0 or self.c < 0:
            print('С отрицательными числами ничего не выйдет')
        elif self.a >= (self.b + self.c) or self.b >= (self.a + self.c) or self.c >= (self.a + self.b):
            print('Невозможно создать треугольник с такими сторонами')
        else:
            print('можно построить треугольник')


Triangle1 = TriangleChecker(1, -1, 4)
Triangle2 = TriangleChecker('s', 's', 'd')
Triangle3 = TriangleChecker(0, 1, 4)
Triangle4 = TriangleChecker(3, 7, 9)
Triangle5 = TriangleChecker(3, 7, 10)
Triangle1.is_triangle()
Triangle2.is_triangle()
Triangle3.is_triangle()
Triangle4.is_triangle()
Triangle5.is_triangle()
