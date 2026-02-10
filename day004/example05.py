"""
example04 - 

Author: kaiby
Date: 2023/12/15 14:08
"""
for m in range(2, 100):
    is_prime = True
    for i in range(2, m):
        if m % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f'{m}是质数')
