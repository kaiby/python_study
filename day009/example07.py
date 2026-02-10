"""
example07 - 

Author: kaiby
Date: 2023/12/28 18:07
"""
content = input('Please input some sentence:')
letter_dic = {}
for letter in content:
    letter_dic[letter] = letter_dic.get(letter, 0) + 1
print(letter_dic)
