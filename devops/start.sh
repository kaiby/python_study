#!/bin/bash

# HTML原型文件上传工具启动脚本

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}======================================${NC}"
echo -e "${GREEN}HTML原型文件上传工具${NC}"
echo -e "${GREEN}======================================${NC}"

# 检查Python是否安装
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}错误: 未安装Python3${NC}"
    exit 1
fi

# 检查pip是否安装
if ! command -v pip3 &> /dev/null; then
    echo -e "${RED}错误: 未安装pip3${NC}"
    exit 1
fi

# 检查依赖是否安装
echo -e "${YELLOW}检查依赖...${NC}"
if ! python3 -c "import flask" &> /dev/null; then
    echo -e "${YELLOW}安装依赖包...${NC}"
    pip3 install -r requirements.txt
fi

# 设置环境变量（可选）
# export NGINX_ROOT="/var/www/html"
# export MAX_FILE_SIZE="104857600"  # 100MB

# 启动应用
echo -e "${GREEN}启动应用...${NC}"
echo -e "${YELLOW}访问地址: http://0.0.0.0:5000${NC}"
echo -e "${YELLOW}按 Ctrl+C 停止服务${NC}"
echo ""

python3 app.py
