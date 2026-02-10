"""
example09 - 随机验证码

Author: kaiby
Date: 2023/12/28 10:38
"""
import random

nums = [i for i in '0123456789']
big_letters = [chr(i) for i in range(65, 91)]
small_letters = [chr(i) for i in range(97, 123)]
all_chars = nums + big_letters + small_letters
# 或通过string模块生成
# all_chars = string.digits + string.ascii_letters

for _ in range(10):
    select_chars = random.choices(all_chars, k=4)
    print(''.join(select_chars))
