"""
example08 - 凯撒密码

Author: kaiby
Date: 2023/12/28 10:30
"""

message = 'nice to meet you'
# 生成对照表
table = str.maketrans('ascdefghijklmnopqrstuvwxyz', 'defghijklmnopqrstuvwxyzabc')
print(message.translate(table))
