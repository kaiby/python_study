"""
example07 - 

Author: kaiby
Date: 2023/12/16 22:32
"""

nums = []

for _ in range(10):
    temp = int(input('Please input a number:'))
    nums.append(temp)

mean_value = sum(nums) / len(nums)
max_value = max(nums)
min_value = min(nums)
print(f'平均值：{mean_value}，最大值：{max_value}，最小值：{min_value}')
