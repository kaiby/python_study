"""
example07 - 

Author: kaiby
Date: 2023/12/15 15:36
"""
import time

start = time.time()
for i in range(2, 10000):
    total = 1
    for j in range(2, i):
        if i % j == 0:
            total += j

    if total == i:
        print(i)
end = time.time()
print(end - start)
