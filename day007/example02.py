"""
example03 - 元组---不可变的容器

Author: kaiby
Date: 2023/12/27 10:15
"""

fruits = ('apple', 'banana', 'pear', 'strawberry', 'orange')

print(fruits * 3)
print(fruits)

print('apple' in fruits)
print('orange' not in fruits)

print(fruits + fruits)

print(fruits[1:4])
print(fruits[1:4:2])
print(fruits[::-1])
print(fruits.index('orange'))
