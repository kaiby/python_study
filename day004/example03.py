"""
example03 - 

Author: kaiby
Date: 2023/12/15 13:59
"""
import math
# or direct import
# from math import factorial as ddd

m = int(input('Please input number:'))
n = int(input('Please input another number:'))

print(math.factorial(m)//math.factorial(n)//math.factorial(m-n))
