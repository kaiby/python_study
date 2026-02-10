"""
example04 - 

~ 列表 list
~ 元组 tuple
~ 集合 set
~ 字典 dict

Author: kaiby
Date: 2023/12/15 17:48
"""

nums = [10, 11, 12, ]
print(type(nums))
print(nums)
words = [12, 5, 'hello', 'world']
print(type(words))
print(words)
nums[1] = 50
nums.append(10000)
nums.insert(0, 222)
print(nums)
nums.pop(0)
print(nums)
for i in nums:
    print(i)
