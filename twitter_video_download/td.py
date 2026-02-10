"""
td - 

Author: kaiby
Date: 2024/11/27 17:48
"""
import os
import requests
import bs4
from tqdm import tqdm
import time
import sys

# 定义一个函数，用于下载视频
def download_video(video_url, output_file_name) -> None:
    """
    从指定的URL下载视频到本地。

    参数:
        video_url (str): 要下载的视频的URL。
        output_file_name (str): 保存视频的文件名或路径。
    """
    response = requests.get(video_url, stream=True)
    total_size = int(response.headers.get("content-length", 0))
    block_size = 1024
    progress_bar = tqdm(total=total_size, unit="B", unit_scale=True)

    download_path = os.path.join(os.getcwd(), output_file_name)

    with open(download_path, "wb") as video_file:
        for data_chunk in response.iter_content(block_size):
            progress_bar.update(len(data_chunk))
            video_file.write(data_chunk)

    progress_bar.close()
    print("视频成功下载！")
    print("视频保存路径：" + download_path)

# 定义一个函数，用于提取Twitter视频的不同质量选项
def fetch_video_links(twitter_post_url):
    """
    提取Twitter帖子中的所有可用视频质量选项。

    参数:
        twitter_post_url (str): Twitter帖子URL。

    返回:
        List[Tuple[str, str]]: 包含质量描述和下载链接的列表。
    """
    api_request_url = f"https://twitsave.com/info?url={twitter_post_url}"
    response = requests.get(api_request_url)
    page_content = bs4.BeautifulSoup(response.text, "html.parser")
    download_section = page_content.find_all("div", class_="origin-top-right")[0]
    quality_links = download_section.find_all("a")

    video_links = []
    for link in quality_links:
        quality = link.text.strip()
        url = link.get("href")
        video_links.append((quality, url))

    return video_links

# 主函数
def main():
    # if len(sys.argv) != 2:
    #     print("用法: python main.py <Twitter视频URL>")
    #     return
    #
    # twitter_post_url = sys.argv[1]

    twitter_post_url = 'https://twitter.com/dotey/status/1683738905412005888'

    # 获取视频链接
    video_links = fetch_video_links(twitter_post_url)

    if not video_links:
        print("未找到可用视频链接，请检查URL是否正确！")
        return

    # 显示可选视频质量
    print("可用视频质量：")
    for idx, (quality, _) in enumerate(video_links):
        print(f"{idx + 1}. {quality}")

    # 用户选择质量
    try:
        choice = int(input("请输入想下载的视频质量编号: ")) - 1
        if choice < 0 or choice >= len(video_links):
            print("无效选择，程序退出。")
            return
    except ValueError:
        print("输入无效，程序退出。")
        return

    # 获取选择的下载链接
    selected_quality, video_url = video_links[choice]
    print(f"开始下载 {selected_quality} 视频...")

    # 使用时间戳生成文件名
    timestamp = int(time.time())
    video_file_name = f"{timestamp}.mp4"

    # 下载视频
    download_video(video_url, video_file_name)

if __name__ == "__main__":
    main()
