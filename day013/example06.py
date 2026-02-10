"""
example06 - 

Author: kaiby
Date: 2024/1/10 11:26
"""


class User:

    def __init__(self, name, password):
        self.name = name
        self.password = password

    def __str__(self):
        return f'name:{self.name}, pass:{self.password}'

    def __repr__(self):
        return f'name:{self.name}, pass:{self.password}'


if __name__ == '__main__':
    tom = User('Tom', '123456')
    jerry = User('Jerry', '000000')
    amy = User('Amy', '7878978')
    users = [tom, jerry, amy]
    print(tom)
    print(users)
