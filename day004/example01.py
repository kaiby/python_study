"""
example01 - 

Author: kaiby
Date: 2023/12/14 18:05
"""

for num in range(100, 1000):
    x = num // 100
    y = num % 100 // 10
    z = num % 10
    if num == x ** 3 + y ** 3 + z ** 3:
        print(num)
