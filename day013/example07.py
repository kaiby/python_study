"""
example07 - 

Author: kaiby
Date: 2024/1/10 14:29
"""


class Card:

    def __init__(self, suite, face):
        self.suite = suite
        self.face = face

    def __str__(self):
        return self.show()

    def __repr__(self):
        return self.show()

    def __lt__(self, other):
        if self.suite == other.suite:
            return self.face < other.face
        return ord(self.suite) < ord(other.suite)

    def show(self):
        suites = {'S': '♠️', 'H': '♥️', 'C': '♣️', 'D': '♦️'}
        faces = ('', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
        return f'{suites[self.suite]}{faces[self.face]}'


def main():
    card1 = Card('C', 3)
    print(card1)


if __name__ == '__main__':
    main()
