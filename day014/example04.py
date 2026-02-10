"""
example - 

Author: kaiby
Date: 2024/1/12 10:21
"""

file = open('noval.txt', 'a', encoding='UTF-8')
try:
    file.write('Hello world, Nice to meet you!\n')
    file.write('How was your day\n')
finally:
    file.close()
