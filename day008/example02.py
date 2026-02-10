"""
example03 - 

Author: kaiby
Date: 2023/12/27 16:29
"""
import os
import time

content = 'HELLO WORLD!                 '

while True:
    os.system('cls')
    print(content)
    time.sleep(0.3)
    content = content[1:] + content[0]
