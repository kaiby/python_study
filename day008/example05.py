"""
example05 - 

Author: kaiby
Date: 2023/12/27 17:27
"""

a = 'hello world'

print(a.center(60, '~'))
print(a.rjust(60, '='))
print(a.ljust(60, '-'))

b = '123'
print(b.zfill(6))
print(b.rjust(6, '0'))

c = 123
d = 456
print('%d + %d = %d' % (c, d, c + d))
print(f'{c} + {d} = {c + d}')
print('{} + {} = {}'.format(c, d, c + d))
print('{0} + {1} = {2}'.format(c, d, c + d))
print('{:.2f}'.format(c))
