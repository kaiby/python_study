"""
example01 - 

Author: kaiby
Date: 2024/1/3 14:11
"""

stocks = {
    "AAPL": 191.88,
    "GOOG": 1186.88,
    'IBM': 149.24,
    'ORCL': 48.44,
    'ACN': 166.89,
    'FB': 208.09,
    'SYMC': 21.29
}

# new_stocks = {}
# for key, value in stocks.items():
#     if value > 100:
#         new_stocks[key] = value

# 生成式写法
new_stocks = {key: value for key, value in stocks.items() if value > 100}

print(new_stocks)

# words = ['apple', 'zoo', 'watermelon', 'giraffe', 'administrator', 'pear']
# print(max(words, key=len))
# words.sort(key=len, reverse=True)
# print(words)

print(max(stocks, key=stocks.get))
print(min(stocks, key=stocks.get))
print(sorted(stocks, key=stocks.get, reverse=True))

# print(max(zip(stocks.values(), stocks.keys()))[1])
# print(min(zip(stocks.values(), stocks.keys()))[1])

dict1 = dict(zip('ABCD', [1, 2, 3, 4]))
print(dict1)
dict2 = dict(A=1, B=2, C=3, D=4)
print(dict2)
