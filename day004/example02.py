"""
example02. - 

Author: kaiby
Date: 2023/12/14 18:22
"""
num = int(input('请输入一个整数：'))
result = 0
while num != 0:
    temp = num % 10
    num = num // 10
    result = result * 10 + temp

print(result)
