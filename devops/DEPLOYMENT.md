# 部署指南

本文档提供详细的生产环境部署步骤。

## 一、环境准备

### 1. 系统要求
- Ubuntu 20.04+ / CentOS 7+ / Debian 10+
- Python 3.8+
- Nginx
- 至少1GB内存

### 2. 安装基础软件

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install python3 python3-pip nginx -y
```

**CentOS/RHEL:**
```bash
sudo yum install python3 python3-pip nginx -y
sudo systemctl enable nginx
sudo systemctl start nginx
```

## 二、部署应用

### 1. 创建应用目录
```bash
sudo mkdir -p /var/www/html-uploader
cd /var/www/html-uploader
```

### 2. 上传项目文件
将以下文件上传到 `/var/www/html-uploader/`:
- app.py
- config.py
- requirements.txt
- gunicorn_config.py
- templates/index.html

或使用git克隆:
```bash
# 如果你的代码在git仓库
git clone your-repo-url /var/www/html-uploader
cd /var/www/html-uploader
```

### 3. 安装Python依赖
```bash
sudo pip3 install -r requirements.txt
sudo pip3 install gunicorn
```

### 4. 配置nginx目录权限

**查找nginx根目录:**
```bash
# 方法1: 查看nginx配置
sudo nginx -T | grep "root"

# 方法2: 常见位置
# Ubuntu/Debian: /var/www/html 或 /usr/share/nginx/html
# CentOS: /usr/share/nginx/html
```

**设置权限:**
```bash
# 假设nginx目录是 /usr/share/nginx/html
sudo chown -R www-data:www-data /usr/share/nginx/html
sudo chmod -R 755 /usr/share/nginx/html
```

### 5. 配置环境变量

编辑 `app.py` 或创建环境变量文件:

```bash
# 创建 .env 文件（如果使用python-dotenv）
cat > /var/www/html-uploader/.env << EOF
NGINX_ROOT=/usr/share/nginx/html
SECRET_KEY=$(python3 -c 'import secrets; print(secrets.token_hex(32))')
FLASK_ENV=production
EOF
```

## 三、配置Systemd服务

### 1. 创建日志目录
```bash
sudo mkdir -p /var/log/html-uploader
sudo chown www-data:www-data /var/log/html-uploader
```

### 2. 安装systemd服务
```bash
# 编辑服务文件
sudo nano /etc/systemd/system/html-uploader.service
```

复制以下内容（根据实际情况修改）:
```ini
[Unit]
Description=HTML Prototype Upload Service
After=network.target

[Service]
Type=simple
User=www-data
Group=www-data
WorkingDirectory=/var/www/html-uploader
Environment="PATH=/usr/local/bin:/usr/bin:/bin"
Environment="NGINX_ROOT=/usr/share/nginx/html"
Environment="SECRET_KEY=your-secret-key-here"
Environment="FLASK_ENV=production"

ExecStart=/usr/local/bin/gunicorn -c gunicorn_config.py app:app

Restart=always
RestartSec=10

StandardOutput=journal
StandardError=journal

LimitNOFILE=65536

[Install]
WantedBy=multi-user.target
```

### 3. 启动服务
```bash
# 重载systemd配置
sudo systemctl daemon-reload

# 启动服务
sudo systemctl start html-uploader

# 设置开机自启
sudo systemctl enable html-uploader

# 查看服务状态
sudo systemctl status html-uploader

# 查看日志
sudo journalctl -u html-uploader -f
```

## 四、配置Nginx反向代理

### 1. 创建nginx配置
```bash
sudo nano /etc/nginx/sites-available/html-uploader
```

添加以下配置:
```nginx
server {
    listen 80;
    server_name your-domain.com;

    location /upload/ {
        proxy_pass http://127.0.0.1:5000/;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        
        client_max_body_size 100M;
        proxy_connect_timeout 300s;
        proxy_send_timeout 300s;
        proxy_read_timeout 300s;
    }
    
    location / {
        root /usr/share/nginx/html;
        index index.html;
        autoindex on;
    }
}
```

### 2. 启用配置
```bash
# 创建软链接
sudo ln -s /etc/nginx/sites-available/html-uploader /etc/nginx/sites-enabled/

# 测试配置
sudo nginx -t

# 重启nginx
sudo systemctl reload nginx
```

## 五、防火墙配置

### Ubuntu (UFW)
```bash
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw enable
```

### CentOS (Firewalld)
```bash
sudo firewall-cmd --permanent --add-service=http
sudo firewall-cmd --permanent --add-service=https
sudo firewall-cmd --reload
```

## 六、SSL证书配置（推荐）

### 使用Let's Encrypt免费证书

```bash
# 安装certbot
sudo apt install certbot python3-certbot-nginx -y  # Ubuntu/Debian
sudo yum install certbot python3-certbot-nginx -y   # CentOS

# 获取证书
sudo certbot --nginx -d your-domain.com

# 自动续期（已自动配置）
sudo certbot renew --dry-run
```

## 七、监控与维护

### 1. 查看服务状态
```bash
sudo systemctl status html-uploader
```

### 2. 查看实时日志
```bash
# 应用日志
sudo journalctl -u html-uploader -f

# Nginx日志
sudo tail -f /var/log/nginx/html-uploader-access.log
sudo tail -f /var/log/nginx/html-uploader-error.log
```

### 3. 重启服务
```bash
sudo systemctl restart html-uploader
```

### 4. 更新应用
```bash
cd /var/www/html-uploader
git pull  # 如果使用git
sudo systemctl restart html-uploader
```

## 八、安全建议

### 1. 限制访问IP
在nginx配置中添加:
```nginx
location /upload/ {
    allow 192.168.1.0/24;  # 允许内网
    allow 10.0.0.0/8;      # 允许VPN
    deny all;              # 拒绝其他
    
    proxy_pass http://127.0.0.1:5000/;
    # ... 其他配置
}
```

### 2. 添加基础认证
```bash
# 安装htpasswd工具
sudo apt install apache2-utils -y

# 创建密码文件
sudo htpasswd -c /etc/nginx/.htpasswd admin

# 在nginx配置中添加
auth_basic "Restricted Access";
auth_basic_user_file /etc/nginx/.htpasswd;
```

### 3. 配置文件上传限制
在 `app.py` 中调整:
```python
MAX_FILE_SIZE = 50 * 1024 * 1024  # 减小到50MB
```

### 4. 定期备份
```bash
# 创建备份脚本
cat > /usr/local/bin/backup-html.sh << 'EOF'
#!/bin/bash
BACKUP_DIR="/backup/html-projects"
NGINX_DIR="/usr/share/nginx/html"
DATE=$(date +%Y%m%d)

mkdir -p $BACKUP_DIR
tar -czf $BACKUP_DIR/html-backup-$DATE.tar.gz $NGINX_DIR
find $BACKUP_DIR -name "*.tar.gz" -mtime +30 -delete
EOF

chmod +x /usr/local/bin/backup-html.sh

# 添加到crontab（每天凌晨2点备份）
(crontab -l 2>/dev/null; echo "0 2 * * * /usr/local/bin/backup-html.sh") | crontab -
```

## 九、故障排查

### 问题1: 服务无法启动
```bash
# 查看详细错误
sudo journalctl -u html-uploader -n 50

# 检查端口占用
sudo netstat -tlnp | grep 5000
```

### 问题2: 上传失败
```bash
# 检查nginx目录权限
ls -la /usr/share/nginx/html

# 检查磁盘空间
df -h

# 查看错误日志
sudo tail -f /var/log/html-uploader/error.log
```

### 问题3: Nginx 502错误
```bash
# 检查gunicorn是否运行
sudo systemctl status html-uploader

# 检查nginx错误日志
sudo tail -f /var/log/nginx/error.log
```

## 十、性能优化

### 1. 调整worker数量
编辑 `gunicorn_config.py`:
```python
workers = 4  # 根据CPU核心数调整
```

### 2. 启用nginx缓存
```nginx
location ~* \.(jpg|jpeg|png|gif|ico|css|js)$ {
    expires 7d;
    add_header Cache-Control "public, immutable";
}
```

### 3. 启用gzip压缩
```nginx
gzip on;
gzip_types text/plain text/css application/json application/javascript;
gzip_min_length 1000;
```

## 完成

部署完成后，访问:
- 上传工具: `http://your-domain.com/upload/`
- 项目文件: `http://your-domain.com/项目名称/`

如有问题，请查看日志或联系技术支持。
