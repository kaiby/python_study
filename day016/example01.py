"""
example01 - 

Author: kaiby
Date: 2024/1/16 17:17
"""
import re

username = input('Please input your name:')

# ma = re.match(r'^\w{6,20}$', username)
ma = re.fullmatch(r'^\w{6,20}$', username)
if ma is None:
    print('Invalid username.')
else:
    print('OK.')
