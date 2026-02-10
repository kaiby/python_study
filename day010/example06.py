"""
example06 - 

Author: kaiby
Date: 2024/1/5 14:31
"""

x = 100


def foo():
    # global x
    x = 200

    def bar():
        nonlocal x
        x = 300
        print(x)

    bar()
    print(x)


foo()
print(x)
