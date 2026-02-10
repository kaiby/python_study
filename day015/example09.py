"""
example09 - 

Author: kaiby
Date: 2024/1/16 15:13
"""
import os.path

import requests
import shutil

def download_img(name, url):
    if not os.path.exists('img'):
        os.makedirs('img')
    resp = requests.get('https://www.bing.com' + url)
    with open(f'img/{name}', 'wb') as file:
        file.write(resp.content)
    print(f'{name} is saved.')


def main():
    resp = requests.get('https://www.bing.com/HPImageArchive.aspx?idx=0&n=10&format=js&pid=HpEdgeAn&mkt=zh-cn')
    images = resp.json()['images']
    for img in images:
        url = img['url']
        name = url[url.find('OHR.') + 4: url.find('.jpg') + 4]
        print(img['title'], 'https://www.bing.com' + url, name)
        # download_img(name, url)
    # 打包到zip
    shutil.make_archive('images', 'zip', 'img')


if __name__ == '__main__':
    main()
