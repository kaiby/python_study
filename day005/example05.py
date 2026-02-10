"""
example05 - 

Author: kaiby
Date: 2023/12/16 21:30
"""

nums = [23, 123, 342, 324, 432]

print(nums[-5])
print(nums[0] + nums[1])

print('=' * 20)

for item in range(len(nums)):
    print(nums[item])

print('=' * 20)

for i, item in enumerate(nums):
    print(i, item)

print('=' * 20)
for item in nums:
    print(item)
