"""
example02 - 

Author: kaiby
Date: 2023/12/16 23:50
"""
import random

nums = []
for _ in range(10):
    nums.append(random.randrange(1, 100))

print(nums)

nums.remove(max(nums))

print(max(nums))
