"""
example04 - 

Author: kaiby
Date: 2023/12/14 16:44
"""

total = 0
for i in range(1, 101):
    if i%2 == 0:
        total += i
    else:
        pass

print(total)
total = sum(range(1, 101))
print(total)
