"""
example06 - 

Author: kaiby
Date: 2023/12/28 17:53
"""

dict1 = {'A': 100, 'B': 200, 'C': 300}
dict2 = {'D': 400, 'E': 500, 'A': 600}

dict1.update(dict2)
print(dict1)

dict1.pop('B')
print(dict1)
dict1.popitem()
print(dict1)
print(dict1.setdefault('A', 'helloworld'))
print(dict1.setdefault('G', 'helloworld'))
print(dict1)
dict1.clear()
print(dict1)
