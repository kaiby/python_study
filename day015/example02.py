"""
example02 - 

Author: kaiby
Date: 2024/1/12 15:41
"""
import datetime

date1 = datetime.datetime(2001, 10, 20)
print(date1)
date2 = datetime.datetime(2010, 11, 23, 15, 30, 25)
print(date2)
print(date2.year, date2.month, date2.day, date2.hour, date2.minute, date2.second)
now = datetime.datetime.now()
print(now)

delta = now - date2
print(type(delta), delta)
print(delta.days, delta.seconds)

print(now.strftime('%Y年%m月%d日 %H:%M:%S'))
