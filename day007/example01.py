"""
example01 - 

Author: kaiby
Date: 2023/12/25 17:37
"""
import random

names = ('Tom', 'Jerry', 'Anna', 'Emma', 'Sam')
courses = ('Math', 'English', 'Physics')
scores = [
    [65, 56, 89],
    [56, 89, 95],
    [46, 46, 46],
    [79, 67, 87],
    [78, 64, 74]
]

# 随机生成方式
scores = [[random.randrange(50, 101) for _ in range(3)] for _ in range(5)]

# for i, name in enumerate(names):
#     for j, course in enumerate(courses):
#         print(f'{name}\'s {course} is: {scores[i][j]}')


# 统计平均成绩
for i, name in enumerate(names):
    print(f'{name}\'s average score is: {sum(scores[i]) / 3:.3f}')

# 统计最高分最低分
for j, course in enumerate(courses):
    temp = [scores[i][j] for i in range(len(names))]
    print(f'{course}\'s max is: {max(temp)}')
    print(f'{course}\'s min is: {min(temp)}')
