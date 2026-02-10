"""
example05 - 

Author: kaiby
Date: 2024/1/8 17:17
"""


def foo():
    print('foo')


def bar():
    foo()
    print('bar')


def main():
    bar()
    print('main')


if __name__ == '__main__':
    main()