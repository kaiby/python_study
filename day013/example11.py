"""
example11 - 

Author: kaiby
Date: 2024/1/10 16:00
"""


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f'{self.name} is eating.')


class Student(Person):

    # __slots__ = ('name', 'age')

    def __init__(self, name, age):
        super().__init__(name, age)

    def _hello(self):
        return f'{self.name}, hello'


if __name__ == '__main__':
    stu = Student('Tom', 20)
    stu.name = 'Jerry'
    # stu.birthday = '2020-12'
    # print(stu.name)
    print(stu._hello())
    stu.eat()
