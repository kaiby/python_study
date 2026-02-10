"""
example02 - 集合运算

Author: kaiby
Date: 2023/12/28 14:06
"""

set1 = {1, 2, 3, 4, 5}
set2 = {2, 4, 6, 8}

print(1 in set1)
print(1 not in set1)

# 交集
print(set1 & set2)
print(set1.intersection(set2))

# 并集
print(set1 | set2)
print(set1.union(set2))

# 差集
print(set1 - set2)
print(set1.difference(set2))
print(set2.difference(set1))

# 对称差
print(set1 ^ set2)
print((set1 | set2) - (set1 & set2))
print(set1.symmetric_difference(set2))

set3 = {1, 2, 3, 4, 5, 6, 7, 8, 9}

# 判断真子集
print(set1 < set3)
# 判断子集
print(set1 <= set3)

# 判断超集
print(set3 > set2)
