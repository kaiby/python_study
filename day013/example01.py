"""
example01 - 

Author: kaiby
Date: 2024/1/8 18:32
"""


class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def read(self):
        print(f'{self.name} is reading a book.')

    def study(self, course):
        print(f'{self.name} is studying {course}.')

    def play(self, game):
        print(f'{self.name} is playing {game}.')

    def watch_movie(self):
        if self.age < 18:
            print('Your age is less than 18, you cann\'t watch this movie')
        else:
            print('Let\'s start watching this movie')
