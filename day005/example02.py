"""
example02 - 

Author: kaiby
Date: 2023/12/15 17:17
"""

total = 0
max_value, min_value = 0, 100
for _ in range(10):
    temp = int(input('Please input number:'))
    total += temp
    if temp > max_value:
        max_value = temp
    if temp < min_value:
        min_value = temp

print(f'平均值：{total / 10}')
print(f'最小值：{min_value}')
print(f'最大值：{max_value}')
