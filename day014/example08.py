"""
example08 - 

Author: kaiby
Date: 2024/1/12 11:27
"""
import csv

with open('P020231019580765294037.csv', 'r', encoding='GBK') as file:
    reader = csv.reader(file, delimiter=',', quotechar='"')
    for line in reader:
        print(reader.line_num, line)


    # line = file.readline()
    # while line:
    #     values = line.strip().split(',')
    #     print(values)
    #     line = file.readline()

