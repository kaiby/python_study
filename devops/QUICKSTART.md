# 快速启动指南

## 🚀 5分钟快速开始

### 1️⃣ 安装依赖
```bash
pip3 install -r requirements.txt
```

### 2️⃣ 配置工作空间根目录
编辑 `app.py` 第18行，修改为你的工作空间根目录：
```python
WORKSPACE_ROOT = '/usr/share/nginx/html'  # 改为你的工作空间根目录
```

### 3️⃣ 启动服务
```bash
# 方法1: 使用启动脚本
./start.sh

# 方法2: 直接运行
python3 app.py
```

### 4️⃣ 访问应用
打开浏览器访问: `http://localhost:5000`

### 5️⃣ 上传测试
- 在左侧创建一个工作空间（如"demo"）
- 选择刚创建的工作空间
- 拖拽 `demo-project.zip` 到上传区域
- 点击"上传并解压"
- 查看上传结果并访问项目

---

## 📁 项目结构
```
html-uploader/
├── app.py                    # Flask应用主程序 ⭐
├── templates/
│   └── index.html           # 前端界面 ⭐
├── requirements.txt         # Python依赖
├── config.py               # 配置文件
├── README.md               # 完整说明文档
├── DEPLOYMENT.md           # 生产环境部署指南
├── start.sh                # 快速启动脚本
├── gunicorn_config.py      # Gunicorn配置
├── html-uploader.service   # Systemd服务文件
├── nginx.conf.example      # Nginx配置示例
└── demo-project.zip        # 演示用zip文件

⭐ = 核心文件
```

---

## 🔧 常见问题

### Q1: 如何修改上传大小限制？
编辑 `app.py` 第19行:
```python
MAX_FILE_SIZE = 200 * 1024 * 1024  # 改为200MB
```

### Q2: 如何查看nginx目录位置？
```bash
# Ubuntu/Debian
/var/www/html 或 /usr/share/nginx/html

# CentOS
/usr/share/nginx/html

# 查看nginx配置
nginx -T | grep "root"
```

### Q3: 权限问题怎么办？
```bash
# 给当前用户授权
sudo chown -R $USER:$USER /usr/share/nginx/html

# 或给www-data用户授权
sudo chown -R www-data:www-data /usr/share/nginx/html
```

### Q4: 如何在生产环境部署？
请查看 `DEPLOYMENT.md` 文档，包含完整的生产环境部署步骤。

---

## 📝 使用流程

1. **创建工作空间**
   - 点击左侧面板的 + 按钮
   - 输入工作空间名称（如：client-a）
   - 点击创建

2. **选择工作空间**
   - 在左侧列表中点击工作空间名称
   - 当前工作空间会高亮显示

3. **上传zip文件**
   - 拖拽或选择zip文件
   - （可选）输入项目名称
   - 点击上传

4. **自动处理**
   - 上传到临时目录
   - 自动解压到选定的工作空间目录
   - 如有同名项目，自动备份

5. **访问项目**
   - 在项目列表中点击"访问"
   - 或直接访问: `http://your-server/工作空间名/项目名/`

6. **管理项目**
   - 查看当前工作空间的所有项目
   - 一键删除不需要的项目
   - 刷新项目列表

---

## 🛡️ 安全提示

⚠️ **重要**: 此工具设计用于内网环境，不建议直接暴露到公网

如需公网访问，请：
1. 配置防火墙限制访问IP
2. 添加HTTP基础认证
3. 使用HTTPS加密传输
4. 定期更新系统和依赖包

详见 `DEPLOYMENT.md` 的安全配置章节。

---

## 📚 文档索引

- **README.md** - 完整功能说明和配置选项
- **DEPLOYMENT.md** - 生产环境部署详细步骤  
- **QUICKSTART.md** - 本文档，快速开始指南

---

## 💡 技术栈

- **后端**: Python 3 + Flask
- **前端**: HTML5 + CSS3 + JavaScript
- **服务器**: Nginx + Gunicorn
- **部署**: Systemd

---

## 🆘 获取帮助

遇到问题？
1. 查看日志: `sudo journalctl -u html-uploader -f`
2. 检查权限: `ls -la /usr/share/nginx/html`
3. 查看FAQ: 在README.md中查找故障排查章节

---

**祝你使用愉快！** 🎉
