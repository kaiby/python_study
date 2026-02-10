"""
example05 - 

Author: kaiby
Date: 2024/1/3 17:40
"""
import random

red_balls = [i for i in range(1, 34)]
blue_ball = [i for i in range(1, 17)]


def generate(max_num, ball_num):
    """
    选择号码
    :param max_num:最大号码
    :param ball_num: 选择数量
    :return:
    """
    balls = [i for i in range(1, max_num + 1)]
    select_balls = random.sample(balls, k=ball_num)
    select_balls.sort()
    return select_balls


def red_ball():
    return generate(33, 6) + generate(16, 1)

def print_ball(balls):

    for ball in balls:
        print(f'{ball:0>2d}', end=' ')
    print()


n = int(input('Input your size:'))

for _ in range(n):
    red_balls = red_ball()
    print_ball(red_balls)
    # select_balls = random.sample(red_balls, 6)
    # select_balls.sort()
    # # select_balls.append(random.choice(blue_ball))
    # select_balls += random.choices(blue_ball, k=1)
    # # print(select_balls)
    # for ball in select_balls[:-1]:
    #     print(f'{ball:0>2d}', end=' ')
    # print(f'| {select_balls[-1]:0>2d}')
