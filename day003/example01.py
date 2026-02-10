"""
example01 - 

Author: kaiby
Date: 2023/12/14 13:50
"""
import getpass

username = input('UserName:')
# password = input('password:')
password = getpass.getpass('password:')
if username == 'admin' and password == 'password':
    print(f'欢迎你，{username}')
    print('Welcome, Nice to meet you!')
else:
    print('用户名或密码错误')
print('=' * 20)
