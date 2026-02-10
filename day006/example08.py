"""
example08 - 

Author: kaiby
Date: 2023/12/25 13:51
"""

nums = [35, 12, 99, 58, 67, 42, 49, 31, 73]

for i in range(0, len(nums) - 1):

    min_value, min_index = nums[i], i

    for j in range(i + 1, len(nums)):
        if min_value > nums[j]:
            min_value, min_index = nums[j], j

    nums[i], nums[min_index] = nums[min_index], nums[i]

print(nums)
