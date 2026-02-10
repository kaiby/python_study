"""
example07 - 

Author: kaiby
Date: 2023/12/28 9:57
"""

# a = '你好，世界'
# b = a.encode('gbk')
# print(type(b))
# print(b)
# c = b'\xc4\xe3\xba\xc3\xa3\xac\xca\xc0\xbd\xe7'
# print(c.decode('gbk'))

a = '👣🐸'
b = a.encode()
print(b, len(b))
print(b.decode())
