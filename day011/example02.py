"""
example02 - 

Author: kaiby
Date: 2024/1/5 16:19
"""


def is_prime(num: int) -> bool:
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


for i in range(2, 100):
    if is_prime(i):
        print(i, end=' ')

# num = int(input('Please input a num:'))
# print(f'{num}: ', is_prime(num))
