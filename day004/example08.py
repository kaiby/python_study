"""
example08 - 

Author: kaiby
Date: 2023/12/15 16:06
"""

for x in range(0, 20):
    for y in range(0, 34):
        z = 100 - x - y
        if z % 3 == 0 and x * 5 + y * 3 + z // 3 == 100:
            print(x, y, z)
        # for z in range(0, 100, ):
        #     if x + y + z == 100 and x * 5 + y * 3 + z // 3 == 100:
        #         print(x, y, z)
