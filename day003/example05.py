"""
example05 - 

Author: kaiby
Date: 2023/12/14 16:53
"""

total = 0
for i in range(1, 101):
    if i % 3 == 0 or i % 5 == 0:
        total += i
print(total)
