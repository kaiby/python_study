"""
example03 - 

Author: kaiby
Date: 2024/1/12 10:09
"""
import hashlib

md5 = hashlib.md5()
sha256 = hashlib.sha256()
file = open('example02.py', 'rb')
try:
    data = file.read(512)
    while data:
        md5.update(data)
        sha256.update(data)
        data = file.read(512)
finally:
    file.close()

print(md5.hexdigest())
print(sha256.hexdigest())
