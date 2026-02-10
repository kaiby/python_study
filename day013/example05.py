"""
example05 - 

Author: kaiby
Date: 2024/1/9 14:15
"""


class Triangle:

    def __init__(self, a, b, c):
        if not Triangle.is_valid(a, b, c):
            raise ValueError('Invalid value.')
        self.a = a
        self.b = b
        self.c = c

    # @classmethod
    # def is_valid(cls, a, b, c):
    #     return a + b > c and a + c > b and b + c > a

    @staticmethod
    def is_valid(a, b, c):
        return a + b > c and a + c > b and b + c > a

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        half = self.perimeter() / 2
        return (half * (half - self.a) * (half - self.b) * (half - self.c)) ** 0.5


if __name__ == '__main__':
    try:
        triangle = Triangle(3, 4, 5)
        print(triangle.perimeter())
        print(triangle.area())
    except ValueError as error:
        print(error)
