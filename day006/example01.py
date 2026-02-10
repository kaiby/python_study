"""
example01 - 

Author: kaiby
Date: 2023/12/16 23:44
"""

a = int(input('Please input a:'))
b = int(input('Please input b:'))
c = int(input('Please input c:'))

if a < b:
    a, b = b, a
if a < c:
    a, c = c, a
if c > b:
    b, c = c, b

print(a, b, c)
