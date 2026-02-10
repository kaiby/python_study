"""
example02 - 

Author: kaiby
Date: 2023/12/14 14:06
"""

x = float(input('请输入x的值：'))

if x > 1:
    y = 3 * x - 5
elif x >= -1:
    y = x + 2
else:
    y = 5 * x + 3

print(f'y={y}')
