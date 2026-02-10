"""
example01 - 

Author: kaiby
Date: 2024/1/11 17:44
"""
import sys

print(sys.getdefaultencoding())
file = open(file='../day013/example12.py', mode='r', encoding='UTF-8')
try:
    data = file.read(20)
    while data:
        print(data, end='')
        data = file.read(20)
except:
    print('Read file error.')
finally:
    file.close()
