"""
tvd_bot - twitter video download bot

# 安装虚拟环境工具
apt update
apt install python3-venv -y

# 创建名为 venv 的虚拟环境
python3 -m venv tvd_env

# 激活虚拟环境
source tvd_env/bin/activate

# 安装三方库
pip install tqdm python-telegram-bot requests beautifulsoup4

Author: kaiby
Date: 2024/11/27 18:07
"""
import configparser
import hashlib
import json
import logging
import mimetypes
import os
import re
import time

import bs4
import requests
from minio import Minio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, CallbackQueryHandler, ContextTypes, \
    filters
from tqdm import tqdm

# 配置日志
# 1.基本配置方式
# logging.basicConfig(
#     filename="tvd_bot.log",
#     filemode="a",
#     format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
#     level=logging.INFO
# )

# 2.高级配置方式
# 创建 logger
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)  # 设置日志级别为 DEBUG

# 创建 console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)  # 设置 console handler 的日志级别为 INFO

# 创建 file handler
file_handler = logging.FileHandler("logs/tvd_bot.log", encoding="utf-8")
file_handler.setLevel(logging.INFO)  # 设置 file handler 的日志级别为 DEBUG

# 创建 formatter
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# 将 formatter 添加到 handlers
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# 将 handlers 添加到 logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)


# 文件大小限制
TELEGRAM_FILE_LIMIT = 50 * 1024 * 1024  # 50 MB

# 读取配置文件
config = configparser.ConfigParser()
config.read('config.ini')

# Telegram token配置
TELEGRAM_BOT_TOKEN = config['telegram']['bot_token']

# MinIO 配置
MINIO_URL = config['minio']['endpoint']  # MinIO 服务地址（例如 http://127.0.0.1:9000）
MINIO_ACCESS_KEY = config['minio']['access_key']
MINIO_SECRET_KEY = config['minio']['secret_key']
MINIO_BUCKET = config['minio']['bucket_name']  # 存储桶名称
ACCESS_LINK = config['minio']['access_link']  # 公开访问链接

# 初始化 MinIO 客户端
minio_client = Minio(
    MINIO_URL.replace("http://", "").replace("https://", ""),
    access_key=MINIO_ACCESS_KEY,
    secret_key=MINIO_SECRET_KEY,
    secure=MINIO_URL.startswith("https"),
)

# 用于存储链接的全局字典
video_link_storage = {}


# 校验是否为有效的IP地址
def is_valid_ip(ip_address):
    ipv4_pattern = r"^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\." \
                   r"(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\." \
                   r"(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\." \
                   r"(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$"
    ipv6_pattern = r"^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$"
    return re.match(ipv4_pattern, ip_address) or re.match(ipv6_pattern, ip_address)

# 查询IP信息的函数
def query_ip_info(ip_address):
    url = f"https://ipinfo.io/widget/demo/{ip_address}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json().get("data")
            if data:
                return json.dumps(data, indent=4, ensure_ascii=False)  # 美化 JSON 数据
            else:
                return "未找到相关IP信息。"
        else:
            return f"请求失败，状态码：{response.status_code}"
    except Exception as e:
        return f"查询时发生错误：{str(e)}"

# 验证输入是否为有效 URL
def is_valid_url(url):
    # 正则表达式用于匹配 URL
    url_pattern = re.compile(
        r'^(https?://)?'  # http:// 或 https:// (可选)
        r'(([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,})'  # 域名
    )
    return re.match(url_pattern, url) is not None

# 下载视频函数
def download_video(video_url, output_file_name):
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
    return download_path

# 提取视频质量链接
def fetch_video_links(twitter_post_url):
    api_request_url = f"https://twitsave.com/info?url={twitter_post_url}"
    response = requests.get(api_request_url)
    page_content = bs4.BeautifulSoup(response.text, "html.parser")
    video_desc_tag = page_content.find("div", class_="leading-tight")
    tags = page_content.find_all("div", class_="origin-top-right")

    if video_desc_tag is not None:
        a_link = video_desc_tag.find("a").text.strip()
        p_content = video_desc_tag.find("p").text.strip()
        logger.info(f"Video description: {p_content}")

    if tags is None or len(tags) == 0:
        raise Exception("Sorry, we could not find any video on this url.")

    download_section = tags[0]
    quality_links = download_section.find_all("a")

    video_info = {}
    video_info["post_url"] = twitter_post_url
    video_info["video_desc"] = f'<a href="{twitter_post_url}">🔗{a_link}</a>\n\n' + p_content

    video_links = []
    for link in quality_links:
        quality = link.text.strip()
        url = link.get("href")
        video_links.append((quality, url))

    video_info["video_links"] = video_links
    return video_info


# 上传到 MinIO
def upload_to_minio(file_path):
    file_name = os.path.basename(file_path)
    object_name = f"{int(time.time())}_{file_name}"

    # 根据文件扩展名获取 Content-Type
    content_type, _ = mimetypes.guess_type(file_path)
    if content_type is None:
        content_type = "application/octet-stream"  # 默认类型

    # 上传文件到 MinIO 并设置 Content-Type
    minio_client.fput_object(
        MINIO_BUCKET,
        object_name,
        file_path,
        content_type=content_type,
    )

    # 构建公开访问的链接
    return f"{ACCESS_LINK}/{MINIO_BUCKET}/{object_name}"

# 启动命令
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("欢迎使用 Twitter 视频下载机器人！请发送 Twitter 视频链接。")

async def bye(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bye " + update.message.from_user.first_name)

# 处理 /ipinfo 命令
async def ipinfo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args:
        ip_address = context.args[0]
        if is_valid_ip(ip_address):
            result = query_ip_info(ip_address)
            await update.message.reply_text(f"IP信息：\n```\n{result}\n```", parse_mode="Markdown")
        else:
            await update.message.reply_text("输入的不是一个有效的IP地址，请检查后重试。")
    else:
        await update.message.reply_text("请提供一个IP地址，例如：/ip 35.223.238.178")

# 处理 /who 命令
async def who(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello, " + update.message.from_user.first_name + " your id is " + str(update.message.from_user.id))

# 处理用户发送的链接
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    twitter_post_url = update.message.text

    # 检查是否是有效 URL
    if not is_valid_url(twitter_post_url):
        await update.message.reply_text("不是有效的链接！")
        return

    try:
        video_info = fetch_video_links(twitter_post_url)

        if not video_info:
            await update.message.reply_text("未找到可用视频链接，请检查输入的 URL 是否正确！")
            return

        # 创建视频质量选择按钮，使用短标识符映射链接
        keyboard = []
        for quality, url in video_info["video_links"]:
            quality = quality.replace('\n', ':').replace('Video:', '')
            quality = re.sub(r'\s+', ' ', quality)
            # 生成短标识符
            short_id = hashlib.md5(url.encode()).hexdigest()
            video_link_storage[short_id] = url  # 存储到全局字典
            video_link_storage[short_id + '_quality'] = quality
            video_link_storage[short_id + "_desc"] = video_info["video_desc"]
            keyboard.append([InlineKeyboardButton(quality, callback_data=short_id)])
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text("请选择视频质量：", reply_markup=reply_markup)
    except Exception as e:
        logger.error(f"处理链接时出错：{str(e)}")
        await update.message.reply_text(f"处理链接时出错：{str(e)}")

# 处理视频质量选择
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    short_id = query.data
    video_url = video_link_storage.get(short_id)  # 根据短标识符获取真实链接
    video_quality = video_link_storage.get(short_id + "_quality")
    video_desc = video_link_storage.get(short_id + "_desc")
    if not video_url:
        await query.edit_message_text("无法找到视频链接，请重试。")
        return

    await query.edit_message_text(f"正在下载视频 ({video_quality})...")

    # 下载视频
    timestamp = int(time.time())
    video_file_name = f"{timestamp}.mp4"
    try:
        download_path = download_video(video_url, video_file_name)
        file_size = os.path.getsize(download_path)

        if file_size > TELEGRAM_FILE_LIMIT:
            await query.message.reply_text("文件超过 50 MB，上传到 Minio...")
            minio_link = upload_to_minio(download_path)
            await query.message.reply_text(f"文件已上传，请点击以下链接下载：\n{minio_link}")
        else:
            await query.message.reply_text("视频下载完成，正在发送给您...")
            with open(download_path, "rb") as video_file:
                await query.message.reply_document(video_file, caption=f"{video_desc}", parse_mode="HTML")

        os.remove(download_path)
    except Exception as e:
        logger.error(f"视频下载或发送时出错：{str(e)}")
        await query.message.reply_text(f"视频下载或发送时出错：{str(e)}")


# 创建应用并注册处理器
def main():
    proxy_url = "socks5://127.0.0.1:1080"
    #proxy_url = "socks5://admin:gGfn3CMl2j06M0BYbe@192.168.1.100:18888"
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).proxy(proxy_url).get_updates_proxy(proxy_url).build()
    #app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("bye", bye))
    app.add_handler(CommandHandler("ip", ipinfo))
    app.add_handler(CommandHandler("who", who))
    # ~filters.COMMAND filters 是过滤，~ 是取反，就是所有非指令的消息
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.add_handler(CallbackQueryHandler(button_handler))

    logger.info("Bot 已启动...")
    app.run_polling()

if __name__ == "__main__":
    main()
