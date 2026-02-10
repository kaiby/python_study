"""
example05 - 

Author: kaiby
Date: 2023/12/28 17:33
"""

student = {'id': '100000', 'name': 'Jerry', 'age': 28, 'address': 'US'}
student['hobby'] = ['Badminton', 'Movie', 'Running']
print(student)
print('name' in student)
print('hobby' in student)
print(student.get('gender'))
print(student.get('gender', 'Male'))
del student['name']
print(student.pop('age'))
print(student.get('name', 'Unknown'))
student['age'] = 26
print(student)

if student.get('gender') is None:
    print('Not find gender')
