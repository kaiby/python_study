"""
example10 - 

Author: kaiby
Date: 2023/12/25 15:22
"""
import random

names = ['Tom', 'Jerry', 'Lily', 'Emma', 'Anna', 'Santa', 'Sam', 'Groot', 'Owl']

# 无放回抽样
print(random.sample(names, 5))

# 有放回抽样
print(random.choices(names, k=5))

# 只抽一个
print(random.choice(names))

# 随机打乱顺序
random.shuffle(names)
print(names)

