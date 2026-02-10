"""
example06 - 

Author: kaiby
Date: 2023/12/15 14:36
"""
n = int(input('Please input a number:'))

for i in range(1, n+1):
    for j in range(i):
        print(i, end=' ')
    print('=', i**2)
