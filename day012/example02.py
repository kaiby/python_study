"""
example02 - 

Author: kaiby
Date: 2024/1/8 14:55
"""


def calculate(init_value, fn, *args, **kwargs):
    total = init_value
    for arg in args:
        if type(arg) in (int, float):
            total = fn(total, arg)

    for value in kwargs.values():
        if type(value) in (int, float):
            total = fn(total, value)
    return total


def add(x, y):
    return x + y


def mul(x, y):
    return x * y


def sub(x, y):
    return x - y


print(calculate(0, add, 1, 2, 3, 4))
print(calculate(1, mul, 1, 2, 3, 4))
print(calculate(10, sub, 1, 2, 3, 4))
