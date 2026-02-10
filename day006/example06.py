"""
example06 - 

Author: kaiby
Date: 2023/12/18 17:17
"""

items = ['apple', 'banana', 'pear', 'watermelon', 'strawberry', 'pitaya', 'apple']

print(items.index('pear'))
print(items.index('strawberry'))
print(items.index('apple', 1))

print('=' * 20)
if 'apple' in items:
    print(items.index('apple'))
if 'apple' in items[3:]:
    print(items.index('apple', 3))

print(items.count('apple'))

items.pop()
print(items)
print(items.pop(3))
del items[0]
print(items)
items.remove('strawberry')
print(items)
items.reverse()
print(items)
items.clear()
print(items)
