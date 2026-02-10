"""
example03 - requests

Author: kaiby
Date: 2024/1/3 15:16
"""
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',  # 有些网站需要特定的 User-Agent
    'Accept-Language': 'en-US,en;q=0.9',  # Accept-Language 根据需要进行设置
    # 可能还需要其他的 headers，具体根据 API 要求设置
}
# resp = requests.get('https://www.bing.com/HPImageArchive.aspx?idx=0&n=10&format=js&pid=HpEdgeAn&mkt=zh-cn')
resp = requests.get('https://i.maoyan.com/api/mmdb/movie/v3/list/hot.json?ct=%E5%8C%97%E4%BA%AC&ci=1&channelId=4',
                    headers=headers)
resp.encoding = 'UTF-8'
print(resp.json())

for item in resp.json().get('data').get('hot'):
    print(item.get('nm'))


# bing_imgs = resp.json();
#
# for item in bing_imgs.get('images'):
#     print(item.get('title'))
#     print('https://www.bing.com' + item.get('url'))
