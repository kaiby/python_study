"""
example12 - 

Author: kaiby
Date: 2023/12/25 16:57
"""
import random

suites = ['黑桃', '红心', '梅花', '方片']
faces = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

cards = [f'{suit}{face}' for suit in suites for face in faces]
cards.append('小王')
cards.append('大王')

random.shuffle(cards)

players = [[] for _ in range(3)]

for _ in range(17):
    for player in players:
        player.append(cards.pop())

players[0].extend(cards)

for player in players:
    player.sort(key=lambda x: x[2:])

    print(player)
