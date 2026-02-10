"""
pullData - 

Author: kaiby
Date: 2025/2/26 11:10
"""
import hashlib
import json
import logging
import time
import requests
import pymysql
import configparser

# 从配置文件读取配置
config = configparser.ConfigParser()
config.read('config.ini')

# 从配置文件中获取 API 配置
url = config.get('api', 'url')
app_key = config.get('api', 'app_key')
app_secret = config.get('api', 'app_secret')

# 从配置文件中获取短信配置
sms_url = config.get('sms', 'url')
phone_num = config.get('sms', 'phone_num')

# 从配置文件中获取 MySQL 配置
mysql_config = {
    'host': config.get('mysql', 'host'),
    'port': config.getint('mysql', 'port'),
    'user': config.get('mysql', 'user'),
    'password': config.get('mysql', 'password'),
    'database': config.get('mysql', 'database'),
    'charset': config.get('mysql', 'charset')
}

# 创建 logger
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)  # 设置日志级别为 DEBUG

# 创建 console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)  # 设置 console handler 的日志级别为 INFO

# 创建 file handler
file_handler = logging.FileHandler("logs/info.log", encoding="utf-8")
file_handler.setLevel(logging.INFO)  # 设置 file handler 的日志级别为 DEBUG

# 创建 formatter
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# 将 formatter 添加到 handlers
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# 将 handlers 添加到 logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)

def v8_open_api_request(body_dto):
    """ 调用接口函数 """
    body = json.dumps(body_dto)
    sign_str = app_secret + body + app_secret
    sign = hashlib.md5(sign_str.encode('utf-8')).hexdigest()

    headers = {
        "app-key": app_key,
        "sign-type": "MD5",
        "sign": sign
    }

    try:
        response = requests.post(url, data=body, headers=headers, timeout=10)
        logger.debug("response=%s", response.text)
        if response.status_code == 200:
            return response.json()
        else:
            return None
    except requests.exceptions.RequestException as e:
        logger.error("Request failed:", e)
        return None


def save_to_mysql(data_list):
    """ 将数据保存到 MySQL 数据库 """
    connection = pymysql.connect(**mysql_config)

    try:
        with connection.cursor() as cursor:
            # 插入数据
            for data in data_list:
                sql = """
                    INSERT INTO organization_members (
                        id, name, code, org_name, login_name, gender, birthday, entry_date, online_status
                    ) VALUES (
                        %s, %s, %s, %s, %s, %s, %s, %s, %s
                    ) ON DUPLICATE KEY UPDATE
                        name = VALUES(name),
                        code = VALUES(code),
                        org_name = VALUES(org_name),
                        login_name = VALUES(login_name),
                        gender = VALUES(gender),
                        birthday = VALUES(birthday),
                        entry_date = VALUES(entry_date),
                        online_status = VALUES(online_status);
                """
                cursor.execute(sql, (
                    data.get('id'),
                    data.get('name'),
                    data.get('code'),
                    data.get('orgName'),
                    data.get('loginName'),
                    data.get('gender'),
                    data.get('birthday'),
                    data.get('entryDate'),
                    data.get('onlineStatus')
                ))
        connection.commit()
    finally:
        connection.close()


def send_sms(content):
    try:
        # 请求参数
        payload = {
            'strmobile': phone_num.strip(),
            'bstrMsg': content.strip()
        }

        # 发送 POST 请求
        response = requests.post(sms_url, data=payload)

        # 记录响应
        logger.info("Send To[%s] SMS[%s] result: %s", phone_num, content, response.text)
    except Exception as e:
        logger.error("Send SMS Result Parse Error: %s", e)


def main():
    """ 主函数，循环调用接口并保存数据 """
    page_number = 1
    page_size = 100
    total_pages = 1

    while page_number <= 1:
        body_dto = {
            "requestId": "hi" + str(int(time.time() * 1000)),
            "timestamp": int(time.time() * 1000),
            "params": {},
            "pageInfo": {
                "pageNumber": page_number,
                "pageSize": page_size,
                "needTotal": True
            }
        }

        result = v8_open_api_request(body_dto)

        if result and result['status'] == 0:
            data = result['data']
            page_info = data['pageInfo']
            content = data['content']

            # 保存数据到 MySQL
            save_to_mysql(content)

            # 更新分页信息
            total_pages = page_info['pages']
            logger.info(f"Page {page_number}/{total_pages} processed.")
            page_number += 1
        else:
            error_message = "Request failed or returned no data."
            logger.error(error_message)
            send_sms(error_message)
            break

        time.sleep(1)  # 防止请求过快

if __name__ == "__main__":
    main()
