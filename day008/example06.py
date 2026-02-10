"""
example06 - 

Author: kaiby
Date: 2023/12/27 17:55
"""

email = ' hello@go.com '
content = 'Nice to meet you'
print(email.strip())
print(email.rstrip())
print(email.lstrip())

print(content.replace('to', '你好'))

print(content.split())
print(content.split(' ', maxsplit=2))

content1 = ['nice', 'to', 'meet', 'you']
print(' '.join(content1))
