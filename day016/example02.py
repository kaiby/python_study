"""
example2 - 

Author: kaiby
Date: 2024/1/16 17:46
"""
import re

username = input('Please input your username:')
username_pattern = re.compile(r'^\w{6,20}$')
ma = username_pattern.match(username)
if ma is not None:
    print('OK.', ma.group())
else:
    print('Invalid.')
