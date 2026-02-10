"""
example09 - 冒泡排序

Author: kaiby
Date: 2023/12/25 14:57
"""

nums = [35, 12, 99, 58, 67, 42, 49, 31, 73]

for i in range(1, len(nums)):
    swapped = False
    for j in range(0, len(nums) - i):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]
            swapped = True
    if not swapped:
        break

print(nums)
