"""
example04 - 

Author: kaiby
Date: 2024/1/3 16:55
"""
import random


def roll_dice(num=2):
    """
    摇骰子
    :param num: 数量
    :return: 结果
    """
    total = 0
    for _ in range(num):
        total += random.randrange(1, 7)
    return total



player_a = {'amount': 1000}
player_b = {'amount': 1000}

while player_a['amount'] > 0:
    print('Player A total amount is :', player_a['amount'])
    zhu = 0
    while zhu <= 0 or zhu > player_a['amount']:
        try:
            zhu = int(input('Please input your amount:'))
        except ValueError:
            pass

    first_num = roll_dice()
    print('First点数：', first_num)

    if first_num in (7, 11):
        print('Player A win!')
        player_a['amount'] += zhu
    elif first_num in (2, 3, 12):
        print('Player B win!')
        player_a['amount'] -= zhu
    else:
        while True:
            current_num = roll_dice(2)
            print('Current Num is :', current_num)
            if current_num == first_num:
                print('Player A win!')
                player_a['amount'] += zhu
                break
            elif current_num == 7:
                print('Player B win!')
                player_a['amount'] -= zhu
                break
print('Game Over!')
