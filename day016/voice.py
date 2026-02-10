"""
voice - 

Author: kaiby
Date: 2024/4/17 15:43
"""

import base64


def concatenate_audio_base64(base64_file, mp3_file):
    audio_data = []
    with open(base64_file, 'r') as file:
        base54_lines = file.readlines()

        for base64_string in base54_lines:
            # 解码base64字符串为音频数据
            decoded_data = base64.b64decode(base64_string)
            audio_data.append(decoded_data)

    # 连接音频数据
    concatenated_data = b''.join(audio_data)

    with open(mp3_file, 'wb') as f:
        f.write(concatenated_data)

    # 编码拼接后的音频为新的base64字符串
    # new_base64_string = base64.b64encode(concatenated_data).decode('utf-8')

    # return new_base64_string


if __name__ == '__main__':
    concatenate_audio_base64('D:\\wiki\\kid\\AI_Story\\base64_line.txt', 'D:\\wiki\\kid\\AI_Story\\base64.mp3')
