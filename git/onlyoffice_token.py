"""
onlyoffice_token - 

Author: kaiby
Date: 2025/6/6 11:34
"""
# !/usr/bin/env python3
"""
OnlyOffice JWT Token生成器 - 修复版
解决常见的JWT验证问题，包括audience验证等
"""

import jwt
import time
import json
from typing import Dict, Any, Optional


class OnlyOfficeJWTFixed:
    def __init__(self, secret_key: str, debug: bool = False):
        """
        初始化JWT生成器

        Args:
            secret_key: JWT签名密钥
            debug: 是否开启调试模式
        """
        self.secret_key = secret_key
        self.debug = debug

        if self.debug:
            print(f"初始化OnlyOffice JWT生成器，密钥: {secret_key}")

    def generate_token(self, document_config: Dict[str, Any]) -> str:
        """
        生成OnlyOffice JWT token

        Args:
            document_config: 文档配置

        Returns:
            JWT token字符串
        """
        # 构建payload，移除可能导致问题的字段
        payload = {
            'exp': int(time.time()) + document_config.get('expires_in', 3600),
            'document': {
                'fileType': document_config.get('file_type', 'docx'),
                'key': document_config['key'],
                'title': document_config['title'],
                'url': document_config['url']
            }
        }

        # 可选字段
        if 'user_id' in document_config and 'user_name' in document_config:
            payload['editorConfig'] = {
                'user': {
                    'id': document_config['user_id'],
                    'name': document_config['user_name']
                },
                'mode': document_config.get('mode', 'edit'),
                'lang': document_config.get('lang', 'zh-CN')
            }

        if self.debug:
            print(f"生成JWT payload: {json.dumps(payload, indent=2, ensure_ascii=False)}")

        try:
            # 生成token
            token = jwt.encode(payload, self.secret_key, algorithm='HS256')

            # 确保返回字符串
            if isinstance(token, bytes):
                token = token.decode('utf-8')

            if self.debug:
                print(f"Token生成成功: {token[:50]}...")

            return token

        except Exception as e:
            if self.debug:
                print(f"Token生成失败: {e}")
            raise Exception(f'Token生成失败: {str(e)}')

    def verify_token(self, token: str, verify_audience: bool = False) -> Dict[str, Any]:
        """
        验证JWT token

        Args:
            token: JWT token
            verify_audience: 是否验证audience字段

        Returns:
            解码后的payload
        """
        try:
            if self.debug:
                print(f"验证Token: {token[:50]}...")

            # 设置验证选项
            options = {
                "verify_aud": verify_audience,  # 通常OnlyOffice不需要严格验证audience
                "verify_iss": False,  # 不验证issuer
            }

            decoded = jwt.decode(
                token,
                self.secret_key,
                algorithms=['HS256'],
                options=options
            )

            if self.debug:
                print("Token验证成功")
                print(f"解码结果: {json.dumps(decoded, indent=2, ensure_ascii=False)}")

            return decoded

        except jwt.ExpiredSignatureError:
            error_msg = 'Token已过期'
            if self.debug:
                print(f"❌ {error_msg}")
            raise Exception(error_msg)

        except jwt.InvalidSignatureError:
            error_msg = 'Token签名无效，请检查密钥是否正确'
            if self.debug:
                print(f"❌ {error_msg}")
            raise Exception(error_msg)

        except jwt.DecodeError:
            error_msg = 'Token格式错误'
            if self.debug:
                print(f"❌ {error_msg}")
            raise Exception(error_msg)

        except jwt.InvalidAudienceError:
            error_msg = 'Audience验证失败'
            if self.debug:
                print(f"❌ {error_msg}")
            raise Exception(error_msg)

        except Exception as e:
            error_msg = f'Token验证失败: {str(e)}'
            if self.debug:
                print(f"❌ {error_msg}")
            raise Exception(error_msg)

    def decode_token_info(self, token: str) -> Optional[Dict[str, Any]]:
        """
        解码token信息（不验证签名，仅用于调试）

        Args:
            token: JWT token

        Returns:
            解码后的信息或None
        """
        try:
            import base64

            parts = token.split('.')
            if len(parts) != 3:
                print(f"Token格式错误，应该有3部分，实际有{len(parts)}部分")
                return None

            # 解码header
            header_data = base64.b64decode(parts[0] + '==')
            header = json.loads(header_data)

            # 解码payload
            payload_data = base64.b64decode(parts[1] + '==')
            payload = json.loads(payload_data)

            info = {
                'header': header,
                'payload': payload
            }

            # 检查过期时间
            if 'exp' in payload:
                exp_time = payload['exp']
                current_time = int(time.time())
                info['is_expired'] = exp_time < current_time
                info['expires_in'] = exp_time - current_time

            return info

        except Exception as e:
            if self.debug:
                print(f"解码Token信息失败: {e}")
            return None


def test_onlyoffice_jwt():
    """测试OnlyOffice JWT功能"""
    print("OnlyOffice JWT 测试")
    print("=" * 50)

    # 初始化生成器
    jwt_gen = OnlyOfficeJWTFixed('nC2T0H5ARcOYjoGcZpLzGAN9HB51lRyS', debug=True)

    # 文档配置
    config = {
        'key': 'doc-12345',
        'title': 'test.docx',
        'url': 'http://10.22.33.28/web/test.docx',
        'file_type': 'docx',
        'user_id': 'user-001',
        'user_name': '测试用户',
        'mode': 'view',
        'expires_in': 3600  # 1小时
    }

    try:
        # 生成token
        print("\n1. 生成Token...")
        token = jwt_gen.generate_token(config)
        print(f"✅ Token: {token}")

        # 验证token
        print("\n2. 验证Token...")
        decoded = jwt_gen.verify_token(token)
        print("✅ Token验证成功")

        # 解码token信息
        print("\n3. Token信息...")
        info = jwt_gen.decode_token_info(token)
        if info:
            print(f"Header: {json.dumps(info['header'], indent=2)}")
            print(f"Payload: {json.dumps(info['payload'], indent=2, ensure_ascii=False)}")
            if 'is_expired' in info:
                print(f"是否过期: {info['is_expired']}")
                print(f"剩余时间: {info['expires_in']}秒")

        return True

    except Exception as e:
        print(f"❌ 测试失败: {e}")
        return False


def main():
    """主函数"""
    print("OnlyOffice JWT生成器 - 修复版")
    print("解决常见的JWT验证问题")
    print()

    # 运行测试
    if test_onlyoffice_jwt():
        print("\n✅ 所有测试通过！")
    else:
        print("\n❌ 测试失败，请检查配置")

    print("\n" + "=" * 50)
    print("使用说明:")
    print("1. 创建OnlyOfficeJWTFixed实例")
    print("2. 调用generate_token()生成token")
    print("3. 调用verify_token()验证token")
    print("4. 如果遇到audience错误，设置verify_audience=False")


if __name__ == '__main__':
    main()