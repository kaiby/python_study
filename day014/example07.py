"""
example07 - 

Author: kaiby
Date: 2024/1/12 10:58
"""

with open('noval.txt', 'r+', encoding='UTF-8') as file:
    data = file.readline()
    while data:
        name, temp = data.strip().split(' ')
        if float(temp) > 37:
            print(name, temp, '异常')
        data = file.readline()
