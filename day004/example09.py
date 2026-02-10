"""
example09 - 

Author: kaiby
Date: 2023/12/15 16:24
"""

fish = 1
while True:
    is_ok = True

    total = fish
    for _ in range(5):
        if (total - 1) % 5 == 0:
            total = (total - 1) // 5 * 4
        else:
            is_ok = False
            break
    if is_ok:
        print(fish)
        break
    fish += 1
