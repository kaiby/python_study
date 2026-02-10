"""
example01 - 

Author: kaiby
Date: 2023/12/15 17:00
"""
import random

i = random.randrange(1, 101)

loop = 0
while True:
    x = int(input('Please input your number:'))
    if loop > 7:
        print('超过次数了')
        break
    if x < i:
        loop += 1
        print('太小了')
    elif x > i:
        loop += 1
        print('太大了')
    else:
        print('猜对了')
        break
