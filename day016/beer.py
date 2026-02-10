"""
beer -
2元钱可以买1瓶啤酒。
4个瓶盖可以换1瓶啤酒。
2个空瓶可以换1瓶啤酒。
10元钱可以喝几瓶啤酒？

Author: kaiby
Date: 2024/4/26 13:48
"""


def buy_beer(money):
    # 每瓶啤酒的价格
    beer_price = 2
    # 用钱可以买到的啤酒数量
    beer_count = money // beer_price
    # 初始瓶子数量
    bottles = beer_count
    # 初始瓶盖数量
    caps = beer_count

    # 当瓶子或瓶盖不够换新的啤酒时结束循环
    while bottles >= 2 or caps >= 4:
        # 用瓶子换来的啤酒数量
        new_beer_bottle = bottles // 2
        # 用瓶盖换来的啤酒数量
        new_beer_cap = caps // 4

        # 计算换来的总啤酒数量
        total_new_beer = new_beer_bottle + new_beer_cap

        # 更新剩余的瓶子和瓶盖数量
        bottles = bottles % 2 + total_new_beer
        caps = caps % 4 + total_new_beer

        # 更新总啤酒数量
        beer_count += total_new_beer

    print("用 {} 元可以喝 {} 瓶啤酒, 剩余空瓶: {}, 瓶盖: {}".format(money, beer_count, bottles, caps))

    return beer_count


# 测试函数
money = 6
beer_count = buy_beer(money)
print("用", money, "元钱可以喝", beer_count, "瓶啤酒。")
