"""
example03 - 

Author: kaiby
Date: 2024/1/8 19:13
"""
import math


class Circle:

    def __init__(self, radius):
        self.radius = radius

    def round(self):
        return 2 * self.radius * math.pi

    def area(self):
        return math.pi * self.radius ** 2


if __name__ == '__main__':
    inner = Circle(10)
    outer = Circle(10 + 3)
    print(inner.round())
    print(outer.area())
