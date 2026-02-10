"""
example02 - 

Author: kaiby
Date: 2024/1/11 18:11
"""

file = open('D:\\F2fmjV4bEAALSbj.jpg', 'rb')
file.seek(0, 2)
print(file.tell())
file.seek(0, 0)
try:
    data = file.read(512)
    while data:
        print(file.read(), end='')
        data = file.read(512)
finally:
    file.close()
