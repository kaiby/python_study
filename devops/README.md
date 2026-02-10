# HTML原型文件上传工具

这是一个基于Flask的Web应用，用于通过网页界面上传ZIP文件并自动解压到nginx指定目录，支持多工作空间管理。

## 功能特性

- ✨ 支持拖拽上传ZIP文件
- 📦 自动解压到nginx静态文件目录
- 🗂️ **工作空间管理** - 支持创建多个工作空间，项目分类管理
- 🔄 自动备份同名项目
- 📋 可视化管理已部署的项目
- 🗑️ 支持删除项目和工作空间
- 🎨 美观的响应式界面

## 工作空间概念

工作空间是项目的分类容器，每个工作空间对应基础目录下的一个文件夹：

```
工作空间根目录/
├── client-a/           (工作空间1)
│   ├── project-v1/     (项目)
│   ├── project-v2/     (项目)
│   └── demo/           (项目)
├── client-b/           (工作空间2)
│   ├── homepage/       (项目)
│   └── dashboard/      (项目)
└── internal/           (工作空间3)
    └── prototype/      (项目)
```

访问路径示例：
- `http://server/client-a/project-v1/`
- `http://server/client-b/homepage/`
- `http://server/internal/prototype/`

## 安装步骤

### 1. 安装Python依赖

```bash
pip install -r requirements.txt
```

或使用pip3:
```bash
pip3 install -r requirements.txt
```

### 2. 配置工作空间根目录

编辑 `app.py` 文件，修改以下配置项：

```python
WORKSPACE_ROOT = '/usr/share/nginx/html'  # 修改为你的工作空间根目录
```

常见的nginx目录：
- Ubuntu/Debian: `/var/www/html` 或 `/usr/share/nginx/html`
- CentOS/RHEL: `/usr/share/nginx/html`
- 自定义配置: 查看nginx配置文件中的root指令

### 3. 确保目录权限

确保运行程序的用户对nginx目录有写权限：

```bash
# 方法1: 修改目录所有者
sudo chown -R $USER:$USER /usr/share/nginx/html

# 方法2: 添加写权限（不推荐生产环境）
sudo chmod -R 755 /usr/share/nginx/html
```

## 运行程序

### 开发环境运行

```bash
python3 app.py
```

程序将在 `http://0.0.0.0:5000` 启动

### 生产环境部署（推荐使用gunicorn）

1. 安装gunicorn:
```bash
pip3 install gunicorn
```

2. 运行:
```bash
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

### 使用systemd服务（推荐）

创建服务文件 `/etc/systemd/system/html-uploader.service`:

```ini
[Unit]
Description=HTML Prototype Upload Service
After=network.target

[Service]
Type=simple
User=www-data
WorkingDirectory=/path/to/your/app
Environment="PATH=/usr/local/bin"
ExecStart=/usr/local/bin/gunicorn -w 4 -b 0.0.0.0:5000 app:app

[Install]
WantedBy=multi-user.target
```

启动服务:
```bash
sudo systemctl daemon-reload
sudo systemctl start html-uploader
sudo systemctl enable html-uploader  # 开机自启
```

## 使用方法

1. 访问 `http://your-server-ip:5000`
2. 在左侧工作空间面板中创建或选择工作空间
3. 拖拽ZIP文件到上传区域，或点击选择文件
4. （可选）输入项目名称，留空则使用ZIP文件名
5. 点击"上传并解压"按钮
6. 上传成功后，可以直接访问项目URL
7. 在"已部署项目"列表中可以查看、访问和删除项目

### 工作空间管理

- **创建工作空间**: 点击左侧面板的 + 按钮
- **选择工作空间**: 点击工作空间名称
- **删除工作空间**: 鼠标悬停在工作空间上，点击🗑️图标（仅能删除空工作空间）

## 配置nginx反向代理（可选）

如果你想通过80端口访问，可以配置nginx反向代理：

```nginx
server {
    listen 80;
    server_name your-domain.com;

    location /upload/ {
        proxy_pass http://127.0.0.1:5000/;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        client_max_body_size 100M;
    }
    
    location / {
        root /usr/share/nginx/html;
        index index.html;
        autoindex on;
    }
}
```

## 配置选项

可以通过修改 `app.py` 文件来调整以下配置：

| 配置项 | 默认值 | 说明 |
|-------|--------|------|
| WORKSPACE_ROOT | /usr/share/nginx/html | 工作空间根目录 |
| UPLOAD_FOLDER | /tmp/uploads | 临时上传目录 |
| MAX_FILE_SIZE | 100MB | 最大文件大小限制 |
| AUTO_BACKUP | True | 是否自动备份同名项目 |

### 备份策略配置

**AUTO_BACKUP = True（默认）**
- 上传同名项目时，旧项目会被重命名为 `项目名_backup_时间戳`
- 可以保留项目历史版本
- 需要手动清理备份文件

**AUTO_BACKUP = False**
- 上传同名项目时，直接覆盖旧项目
- 不保留历史版本
- 节省磁盘空间

修改方式：
```python
# 在 app.py 第21行
AUTO_BACKUP = False  # 改为False则直接覆盖，不备份
```

## 注意事项

1. **安全性**: 
   - 此工具仅供内部使用，不建议直接暴露到公网
   - 建议配置防火墙规则限制访问IP
   - 生产环境请添加身份认证机制

2. **文件大小限制**: 
   - 默认限制100MB，可在 `app.py` 中修改 `MAX_FILE_SIZE`

3. **备份策略**: 
   - 上传同名项目时会自动备份旧版本
   - 备份目录格式: `项目名_backup_时间戳`

4. **权限问题**:
   - 确保程序有权限写入nginx目录
   - 如遇权限问题，检查目录所有者和权限设置

## 目录结构

```
.
├── app.py                 # Flask应用主程序
├── templates/
│   └── index.html        # 前端页面
├── requirements.txt      # Python依赖
└── README.md            # 说明文档
```

## 故障排查

### 1. 上传失败 "权限被拒绝"
检查nginx目录权限，确保运行用户有写权限

### 2. 无法访问上传的项目
检查nginx配置，确保配置了正确的root目录

### 3. 文件过大上传失败
- 修改 `app.py` 中的 `MAX_FILE_SIZE`
- 如使用nginx反向代理，增加 `client_max_body_size`

## 开发者

基于Flask + HTML5 开发

## 许可证

MIT License
