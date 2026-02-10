# 配置说明文档

本文档详细说明HTML原型文件上传工具的所有配置选项。

## 配置文件位置

主要配置在以下文件中：
- `app.py` - 主配置文件（开发/简单部署）
- `config.py` - 环境配置文件（生产部署推荐）

## 配置项详解

### 1. 工作空间根目录

**配置项**: `WORKSPACE_ROOT`  
**默认值**: `/usr/share/nginx/html`  
**说明**: 所有工作空间和项目文件的存储根目录

**配置方式**:
```python
# app.py 第18行
WORKSPACE_ROOT = '/var/www/html'  # 修改为你的目录
```

**环境变量**:
```bash
export WORKSPACE_ROOT=/var/www/html
```

**常见路径**:
- Ubuntu/Debian: `/var/www/html` 或 `/usr/share/nginx/html`
- CentOS/RHEL: `/usr/share/nginx/html`
- macOS (Homebrew): `/usr/local/var/www`

### 2. 临时上传目录

**配置项**: `UPLOAD_FOLDER`  
**默认值**: `/tmp/uploads`  
**说明**: ZIP文件上传后的临时存储位置，解压后会自动删除

**配置方式**:
```python
# app.py 第17行
UPLOAD_FOLDER = '/var/tmp/uploads'  # 修改为你的临时目录
```

**注意事项**:
- 需要有写入权限
- 空间充足（至少能容纳最大上传文件）
- 系统重启后 `/tmp` 目录可能被清空

### 3. 最大文件大小

**配置项**: `MAX_FILE_SIZE`  
**默认值**: `100 * 1024 * 1024` (100MB)  
**说明**: 允许上传的ZIP文件最大大小

**配置方式**:
```python
# app.py 第20行
MAX_FILE_SIZE = 200 * 1024 * 1024  # 200MB
MAX_FILE_SIZE = 500 * 1024 * 1024  # 500MB
MAX_FILE_SIZE = 1024 * 1024 * 1024  # 1GB
```

**环境变量**:
```bash
export MAX_FILE_SIZE=209715200  # 200MB (字节)
```

**配套配置**:
如果使用nginx反向代理，需要同步修改nginx配置：
```nginx
client_max_body_size 200M;
```

### 4. 自动备份配置 ⭐

**配置项**: `AUTO_BACKUP`  
**默认值**: `True`  
**说明**: 上传同名项目时是否自动备份旧版本

**配置方式**:
```python
# app.py 第21行
AUTO_BACKUP = True   # 备份模式（默认）
AUTO_BACKUP = False  # 覆盖模式
```

**环境变量**:
```bash
export AUTO_BACKUP=False  # 或 true/false, yes/no, 1/0
```

#### 备份模式 (AUTO_BACKUP = True)

**行为**:
- 上传同名项目时，旧项目重命名为 `项目名_backup_时间戳`
- 保留所有历史版本
- 需要手动清理备份

**示例**:
```
上传前:
workspace/
└── client-a/
    └── homepage/

第一次上传 homepage.zip:
workspace/
└── client-a/
    └── homepage/

第二次上传 homepage.zip:
workspace/
└── client-a/
    ├── homepage/                    ← 新版本
    └── homepage_backup_20240210_143520/  ← 备份
```

**优点**:
- ✅ 安全，可以回滚
- ✅ 保留历史版本
- ✅ 适合重要项目

**缺点**:
- ❌ 占用更多磁盘空间
- ❌ 需要定期清理备份

#### 覆盖模式 (AUTO_BACKUP = False)

**行为**:
- 上传同名项目时，直接删除旧项目
- 用新项目完全替换
- 不保留任何历史版本

**示例**:
```
上传前:
workspace/
└── client-a/
    └── homepage/  (旧版本)

上传 homepage.zip 后:
workspace/
└── client-a/
    └── homepage/  (新版本，旧版本已删除)
```

**优点**:
- ✅ 节省磁盘空间
- ✅ 目录结构清爽
- ✅ 适合频繁更新的项目

**缺点**:
- ❌ 无法恢复旧版本
- ❌ 覆盖不可逆

#### 使用场景推荐

**使用备份模式的场景**:
- 客户演示项目（需要版本对比）
- 重要的生产原型
- 需要审批的设计稿
- 长期维护的项目

**使用覆盖模式的场景**:
- 开发环境快速迭代
- 临时测试项目
- 磁盘空间有限
- 版本控制已在Git等系统中管理

### 5. 允许的文件扩展名

**配置项**: `ALLOWED_EXTENSIONS`  
**默认值**: `{'zip'}`  
**说明**: 允许上传的文件类型

**配置方式**:
```python
# app.py 中
ALLOWED_EXTENSIONS = {'zip'}  # 仅ZIP
ALLOWED_EXTENSIONS = {'zip', 'tar', 'gz'}  # 多种格式（需修改解压逻辑）
```

**注意**: 当前仅支持ZIP格式，添加其他格式需要修改解压函数。

### 6. Flask密钥

**配置项**: `SECRET_KEY`  
**默认值**: `'dev-secret-key-change-in-production'`  
**说明**: Flask会话加密密钥，生产环境必须修改

**配置方式**:
```python
# config.py 中
SECRET_KEY = 'your-random-secret-key-here'
```

**生成随机密钥**:
```bash
python3 -c 'import secrets; print(secrets.token_hex(32))'
```

**环境变量**:
```bash
export SECRET_KEY='your-random-secret-key-here'
```

## 环境变量配置

推荐在生产环境使用环境变量配置，而不是直接修改代码。

### 创建配置文件

```bash
# 创建 .env 文件
cat > .env << EOF
WORKSPACE_ROOT=/var/www/html
UPLOAD_FOLDER=/var/tmp/uploads
MAX_FILE_SIZE=209715200
AUTO_BACKUP=True
SECRET_KEY=$(python3 -c 'import secrets; print(secrets.token_hex(32))')
FLASK_ENV=production
EOF
```

### 使用环境变量

```bash
# 方式1: 导出环境变量
source .env
python3 app.py

# 方式2: 使用systemd服务
# 在 html-uploader.service 中配置
Environment="WORKSPACE_ROOT=/var/www/html"
Environment="AUTO_BACKUP=False"

# 方式3: 使用docker
docker run -e WORKSPACE_ROOT=/data -e AUTO_BACKUP=False ...
```

## 配置最佳实践

### 1. 开发环境配置

```python
# app.py
WORKSPACE_ROOT = '/tmp/html-workspace'  # 本地测试目录
UPLOAD_FOLDER = '/tmp/uploads'
MAX_FILE_SIZE = 50 * 1024 * 1024  # 50MB，节省空间
AUTO_BACKUP = True  # 方便测试回滚
```

### 2. 生产环境配置

```python
# 使用环境变量，在 systemd 或 docker 中配置
WORKSPACE_ROOT = os.environ.get('WORKSPACE_ROOT', '/var/www/html')
AUTO_BACKUP = os.environ.get('AUTO_BACKUP', 'True').lower() in ('true', '1', 'yes')
```

### 3. 高频更新项目配置

```python
AUTO_BACKUP = False  # 不备份，直接覆盖
MAX_FILE_SIZE = 200 * 1024 * 1024  # 较大的限制
```

### 4. 多客户环境配置

```python
AUTO_BACKUP = True  # 备份客户项目
WORKSPACE_ROOT = '/var/www/clients'  # 专用客户目录
```

## 配置验证

启动应用后，会显示当前配置：

```
============================================================
HTML原型文件上传工具启动
上传目录: /tmp/uploads
工作空间根目录: /usr/share/nginx/html
访问地址: http://0.0.0.0:5000
============================================================
```

检查配置是否正确：

```bash
# 检查目录是否存在且有权限
ls -ld /usr/share/nginx/html
ls -ld /tmp/uploads

# 检查磁盘空间
df -h /usr/share/nginx/html

# 测试写入权限
touch /usr/share/nginx/html/test && rm /usr/share/nginx/html/test
```

## 动态配置（高级）

如果需要在运行时修改配置，可以创建配置管理界面或API。

### 示例：配置API

```python
@app.route('/api/config', methods=['GET'])
def get_config():
    """获取当前配置"""
    return jsonify({
        'workspace_root': WORKSPACE_ROOT,
        'max_file_size': MAX_FILE_SIZE,
        'auto_backup': AUTO_BACKUP
    })

@app.route('/api/config/backup', methods=['POST'])
def set_backup_config():
    """设置备份模式"""
    global AUTO_BACKUP
    data = request.get_json()
    AUTO_BACKUP = data.get('enabled', True)
    return jsonify({'success': True, 'auto_backup': AUTO_BACKUP})
```

## 故障排查

### 问题1: 配置不生效

**检查**:
- 是否重启了应用？
- 环境变量是否正确加载？
- 是否修改了正确的文件？

**解决**:
```bash
# 查看当前环境变量
env | grep WORKSPACE_ROOT

# 重启应用
sudo systemctl restart html-uploader
```

### 问题2: 权限错误

**检查**:
```bash
# 检查目录权限
ls -ld /usr/share/nginx/html

# 检查运行用户
ps aux | grep python3
```

**解决**:
```bash
sudo chown -R www-data:www-data /usr/share/nginx/html
sudo chmod -R 755 /usr/share/nginx/html
```

### 问题3: 文件过大无法上传

**检查**:
- `MAX_FILE_SIZE` 配置
- Nginx `client_max_body_size` 配置

**解决**:
```python
# 增加限制
MAX_FILE_SIZE = 500 * 1024 * 1024  # 500MB
```

```nginx
# nginx配置
client_max_body_size 500M;
```

## 总结

| 配置项 | 推荐值 | 说明 |
|--------|--------|------|
| WORKSPACE_ROOT | /var/www/html | 根据实际nginx配置 |
| UPLOAD_FOLDER | /tmp/uploads | 默认即可 |
| MAX_FILE_SIZE | 100-200MB | 根据实际需求 |
| **AUTO_BACKUP** | **True/False** | **重要：根据使用场景选择** |
| SECRET_KEY | 随机32字节 | 生产环境必须修改 |

合理配置这些选项，可以让工具更符合你的使用场景！
