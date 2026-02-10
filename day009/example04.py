"""
example04 - 

Author: kaiby
Date: 2023/12/28 16:51
"""

student = {'name': 'TOM', 'age': 26, 'gender': 'Female', 'address': 'US', 'hobby': ['badminton', 'movie', 'girls'],
           'contact': {'phone': '13112345678', 'email': 'hello@123.com'}}

print(student['name'], student['age'])
print(student['contact'])

student2 = dict(id=1000, name='Jerry', age=26, gender='Female')
print(student2)
print(len(student2))

for key in student2:
    print(key, student2[key])

print(student2.values())

print('=' * 20)

for key, value in student2.items():
    print(key, value)

list1 = [i for i in range(1, 10)]
print(list1)
set1 = {i for i in range(1, 10)}
print(set1)
dict1 = {i: i ** 2 for i in range(1, 10)}
print(dict1)

# 生成器
gen_obj = (i for i in range(1, 10))
print(next(gen_obj))
print(next(gen_obj))
