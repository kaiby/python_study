"""
example04 - 

Author: kaiby
Date: 2023/12/15 14:08
"""

x = int(input('Please input a Integer:'))

is_prime = True
for i in range(2, x):
    if x % i == 0:
        is_prime = False
        break
if x > 1 and is_prime:
    print(f'{x}是质数')
else:
    print(f'{x}不是质数')
