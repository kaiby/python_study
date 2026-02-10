"""
example06 - 

Author: kaiby
Date: 2023/12/16 22:24
"""
import random

# fs = [0, 0, 0, 0, 0, 0]

fs = [0] * 6

for _ in range(60000):
    i = random.randrange(1, 7)
    fs[i - 1] += 1

for i, item in enumerate(fs):
    print(f'{i + 1}点出现了{item}次')
