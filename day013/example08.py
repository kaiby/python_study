"""
example08 - 

Author: kaiby
Date: 2024/1/10 14:42
"""
import random

from example07 import Card


class Poker:

    def __init__(self):
        self.cards = [Card(suite, face) for suite in 'SHCD' for face in range(1, 14)]
        self.counter = 0

        # for suite in 'SHCD':
        #     for face in range(1, 14):
        #         card = Card(suite, face)
        #         self.cards.append(card)

    def shuffle(self):
        self.counter = 0
        random.shuffle(self.cards)

    def deal(self):
        card = self.cards[self.counter]
        self.counter += 1
        return card

    def has_more(self):
        return self.counter < len(self.cards)


def main():
    poker = Poker()
    poker.shuffle()
    while poker.has_more():
        print(poker.deal(), end=' ')


if __name__ == '__main__':
    main()
