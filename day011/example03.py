"""
example03 - 

Author: kaiby
Date: 2024/1/5 17:08
"""


def gcd(x: int, y: int) -> int:
    """
    求最大公约数
    :param x:
    :param y:
    :return:
    """
    while y % x != 0:
        x, y = y % x, x
    return x


def lcm(x: int, y: int) -> int:
    """
    求最小公倍数
    :param x:
    :param y:
    :return:
    """
    return x * y // gcd(x, y)


print(__name__)

if __name__ == '__main__':
    print(gcd(27, 15))
    print(lcm(27, 15))
