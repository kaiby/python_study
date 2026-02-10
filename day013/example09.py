"""
example09 - 

Author: kaiby
Date: 2024/1/10 15:19
"""
from example08 import Poker

class Player:

    def __init__(self, nickname):
        self.nickname = nickname
        self.cards = []

    def get_card(self, card):
        self.cards.append(card)

    def arrange(self):
        self.cards.sort()

    def show(self):
        print(self.nickname, end=':')
        for card in self.cards:
            print(card, end=' ')
        print()


def main():
    poker = Poker()
    poker.shuffle()
    player = Player('Tom')
    for _ in range(10):
        player.get_card(poker.deal())
    player.arrange()
    player.show()


if __name__ == '__main__':
    main()
