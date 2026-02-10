"""
app - 

Author: kaiby
Date: 2023/12/19 17:44
"""
import base64
import datetime
import os
import io

from flask import Flask, request, jsonify
from minio import Minio
from minio.error import InvalidResponseError

app = Flask(__name__)

UPLOAD_FOLDER = r'D:\\'  # 替换为你想要保存文件的目标文件夹路径
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def save_image(image_data):
    try:
        # 解码Base64数据为二进制数据
        binary_data = base64.b64decode(image_data)

        # 获取当前日期时间
        current_datetime = datetime.datetime.now()
        timestamp = current_datetime.strftime('%Y%m%d_%H%M%S')

        # 构建文件名
        filename = f"{timestamp}.png"

        # 构建保存路径
        save_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

        # 将二进制数据写入文件
        with open(save_path, 'wb') as f:
            f.write(binary_data)

        save_to_minio(binary_data, filename)

        return save_path
    except Exception as e:
        print("Error during saving image:", str(e))
        return None


def save_to_minio(binary_data, file_name):
    minio_client = Minio(
        "127.0.0.1:9000",
        access_key="admin",
        secret_key="6910d580-08d4-11ed-9887-927de4c40b55",
        secure=False
    )
    # 替换以下信息为你的存储桶名称和要保存的文件名
    bucket_name = 'xmas-selfie'
    # file_name = 'your_file_name.jpg'  # 或者其他图片格式

    try:
        # 将二进制数据保存到MinIO存储桶
        minio_client.put_object(
            bucket_name,
            file_name,
            data=io.BytesIO(binary_data),  # binary_data是你的二进制图片数据
            length=len(binary_data),
            content_type='image/jpeg'  # 替换为你的图片类型
        )
        print(f"图片 '{file_name}' 已成功保存到MinIO存储桶 '{bucket_name}' 中")
    except InvalidResponseError as err:
        print(f"保存到MinIO存储桶时出错: {err}")


@app.route('/upload', methods=['POST'])
def upload_photo():
    try:
        data = request.get_json()
        image_data = data.get('image')
        image_data = image_data[22:]
        print(image_data[:50])

        if image_data:
            # 保存图像并获取保存路径
            saved_path = save_image(image_data)

            if saved_path:
                return jsonify({'success': True, 'message': '照片上传成功', 'saved_path': saved_path})
            else:
                return jsonify({'success': False, 'message': '照片保存失败'})
        else:
            return jsonify({'success': False, 'message': '未收到有效的图片数据'})

    except Exception as e:
        print("Error during photo upload:", str(e))
        return jsonify({'success': False, 'message': '照片上传失败'})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
