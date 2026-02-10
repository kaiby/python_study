"""
example04 - 字符串

Author: kaiby
Date: 2023/12/27 10:59
"""

a = '\'hello \nworld\''
b = 'hello world'
c = '''
hello
world
'''

print(a)
print(b)
print(c)

# 原始字符串
d = r'\\hello world\\'
print(d)

# 格式化字符串
e = f'test:{d}'
print(e)

s1 = '\141\142\143\x61\x62\x63'
print(s1)

# unicode 编码
s2 = '\u2155'
print(s2)

