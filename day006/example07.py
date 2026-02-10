"""
example07 - 

Author: kaiby
Date: 2023/12/18 17:51
"""

items = ['apple', 'banana', 'pear', 'watermelon', 'strawberry', 'pitaya', 'apple']
print(items)
print(items[::-1])
print(items)
items.reverse()
print(items)

items.sort(reverse=True)
print(items)

nums = ['1', '10', '234', '2', '35', '100']
nums.sort(key=int)
print(nums)
# print(nums)
# nums = [int(num) for num in nums]
# nums.sort()
# print(nums)
