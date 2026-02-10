"""
Gunicorn配置文件
用于生产环境部署
"""

import multiprocessing

# 绑定地址
bind = "0.0.0.0:5000"

# 工作进程数（推荐：CPU核心数 * 2 + 1）
workers = multiprocessing.cpu_count() * 2 + 1

# 工作模式
worker_class = "sync"

# 超时时间（秒）
timeout = 120

# 保持连接时间（秒）
keepalive = 5

# 最大请求数，防止内存泄漏
max_requests = 1000
max_requests_jitter = 100

# 日志配置
accesslog = "/var/log/html-uploader/access.log"
errorlog = "/var/log/html-uploader/error.log"
loglevel = "info"

# 进程名称
proc_name = "html-uploader"

# 守护进程模式（systemd管理时设为False）
daemon = False

# 临时文件目录
tmp_upload_dir = "/tmp"
