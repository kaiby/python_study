"""
example09 - 

Author: kaiby
Date: 2024/1/12 11:55
"""
import csv

with open('user_list.csv', 'w', newline='') as file:

    writer = csv.writer(file)
    writer.writerow(['1', 'Tom', 25])
    writer.writerow(['2', 'Jerry', 23])
