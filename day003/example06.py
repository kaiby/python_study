"""
example06 - 

Author: kaiby
Date: 2023/12/14 17:02
"""

x = int(input('请输入第一个正整数：'))
y = int(input('请输入第二个正整数：'))

for i in range(x, 0, -1):
    if x % i == 0 and y % i == 0:
        print(i)
        break
