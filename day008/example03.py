"""
example03 - 

Author: kaiby
Date: 2023/12/27 16:40
"""

a = 'nice to MEET you'

print('大写', a.upper())
print('小写', a.lower())
print('首字母大写', a.capitalize())
print('每个单词首字母大写', a.title())
print(a)
print('=' * 20)
b = 'abc123'
print(b.isdigit())
print(b.isalpha())
print(b.isalnum())
print(b.isascii())
print('=' * 20)

c = '你好，世界'
print(c.startswith('你好'))
print(c.endswith('h'))
print(c.index('好'))
