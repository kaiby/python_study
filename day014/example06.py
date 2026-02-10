"""
example06 - 

Author: kaiby
Date: 2024/1/12 10:41
"""

with open('D:\\F2fmjV4bEAALSbj.jpg', 'rb') as file:
    print(file.name)
    with open('D:\\new123.jpg', 'wb') as new_file:
        data = file.read(512)
        while data:
            new_file.write(data)
            data = file.read(512)
