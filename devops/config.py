"""
配置文件
"""
import os

class Config:
    """基础配置"""
    # 上传临时目录
    UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER', '/tmp/uploads')
    
    # 工作空间根目录（重要：根据实际情况修改）
    WORKSPACE_ROOT = os.environ.get('WORKSPACE_ROOT', '/usr/share/nginx/html')
    
    # 最大文件大小（字节）
    MAX_FILE_SIZE = int(os.environ.get('MAX_FILE_SIZE', 100 * 1024 * 1024))  # 100MB
    
    # 允许的文件扩展名
    ALLOWED_EXTENSIONS = {'zip'}
    
    # 自动备份配置：True=备份旧项目，False=直接覆盖
    AUTO_BACKUP = os.environ.get('AUTO_BACKUP', 'True').lower() in ('true', '1', 'yes')
    
    # Flask配置
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')
    MAX_CONTENT_LENGTH = MAX_FILE_SIZE


class DevelopmentConfig(Config):
    """开发环境配置"""
    DEBUG = True
    TESTING = False


class ProductionConfig(Config):
    """生产环境配置"""
    DEBUG = False
    TESTING = False
    
    # 生产环境必须设置SECRET_KEY
    SECRET_KEY = os.environ.get('SECRET_KEY')
    if not SECRET_KEY:
        raise ValueError("生产环境必须设置SECRET_KEY环境变量")


class TestingConfig(Config):
    """测试环境配置"""
    DEBUG = True
    TESTING = True


# 配置字典
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
