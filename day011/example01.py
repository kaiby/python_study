"""
example01 - 

Author: kaiby
Date: 2024/1/5 15:51
"""
import random
import string


def captcha(length: int = 4) -> str:
    """
    随机验证码
    :param length: 长度
    :return:
    """
    all_chars = string.ascii_uppercase + string.digits
    select = random.choices(all_chars, k=length)
    return ''.join(select)


length = int(input('Input validate number size:'))

print(captcha(length))
