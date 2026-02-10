"""
example03 - 

Author: kaiby
Date: 2023/12/15 17:34
"""
import random

f1, f2, f3, f4, f5, f6 = 0, 0, 0, 0, 0, 0
for _ in range(60000):
    i = random.randrange(1, 7)
    if i == 1:
        f1 += 1
    elif i == 2:
        f2 += 1
    elif i == 3:
        f3 += 1
    elif i == 4:
        f4 += 1
    elif i == 5:
        f5 += 1
    else:
        f6 += 1
print(f'1=={f1}')
print(f'2=={f2}')
print(f'3=={f3}')
print(f'4=={f4}')
print(f'5=={f5}')
print(f'6=={f6}')
