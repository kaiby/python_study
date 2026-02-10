"""
example01 - 

Author: kaiby
Date: 2024/1/8 13:57
"""


def add(*args, **kwargs):
    total = 0
    for arg in args:
        if type(arg) in (int, float):
            total += arg

    for kwarg in kwargs.values():
        if type(kwarg) in (int, float):
            total += kwarg
    return total


print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, '3', a=1, b=2))
print(add(1, 2, 3, 4))
