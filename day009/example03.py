"""
example03 - 

Author: kaiby
Date: 2023/12/28 14:25
"""

set1 = {'apple', 'banana', 'orange', 'strawberry', 'apple'}
set1.add('pear')
print(set1)
set1.discard('orange')
set1.remove('apple')
print(set1.pop())
print(set1)

set2 = {(1, 2, 5, 1), (3, 4), (1, 2, 1, 5)}
print(set2)
