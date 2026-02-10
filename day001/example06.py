"""
example06 - 

Author: kaiby
Date: 2023/12/13 17:01
"""

a = float(input('请输入一个数字：'))
b = float(input('请输入另一个数字：'))

print('%.1f + %.1f =%.1f' % (a, b, a + b))
print('%.1f - %.2f =%.3f' % (a, b, a - b))
print('%f * %f =%f' % (a, b, a * b))
print('%f / %f =%f' % (a, b, a / b))
print('%f // %f =%f' % (a, b, a // b))
print('%f %% %f =%f' % (a, b, a % b))
print('%f ** %f =%f' % (a, b, a ** b))

