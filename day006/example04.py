"""
example04 - 

Author: kaiby
Date: 2023/12/18 16:00
"""

list1 = ['apple', 'orange', 'pear', 'banana', 'pitaya']
print(list1)
list2 = list(range(1, 10))
print(list2)

list3 = [i ** 2 for i in range(1, 10)]
print(list3)

for i, item in enumerate(list3):
    print(i, item)

list4 = [1, 10, 100] * 5
print(list4)

print(10 in list4)
print(5 in list4)
print(5 not in list4)
print('pitaya' in list1)

list5 = [1, 3, 5, 7]
list6 = [2, 4, 6]
list6 += list5
print(list5)

list7 = list(range(1, 8, 2))
print(list7)
list8 = [1, 3, 5, 7, 9]
print(list5 == list7)
print(list7 > list8)
