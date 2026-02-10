"""
homework01 - 

Author: kaiby
Date: 2023/12/14 10:15
"""
import math

radius = float(input('请输入圆的半径：'))
perimeter = 2 * math.pi * radius
area = math.pi * radius ** 2
print(f'圆的周长是：{perimeter:.4f}')
print(f'圆的面积是：{area:.4f}')
