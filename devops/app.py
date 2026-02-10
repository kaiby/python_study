#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HTML原型文件上传解压工具
支持拖拽上传zip文件到指定nginx目录
"""

from flask import Flask, request, render_template, jsonify
from werkzeug.utils import secure_filename
import os
import zipfile
import shutil
from datetime import datetime

app = Flask(__name__)

# 配置项 - 根据实际情况修改
UPLOAD_FOLDER = 'D:\\temp\\test'  # 临时上传目录
NGINX_ROOT = 'D:\\temp\\test'  # nginx静态文件根目录，请根据实际修改
MAX_FILE_SIZE = 100 * 1024 * 1024  # 100MB
ALLOWED_EXTENSIONS = {'zip'}

# 创建必要的目录
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(NGINX_ROOT, exist_ok=True)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_FILE_SIZE


def allowed_file(filename):
    """检查文件扩展名是否允许"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def extract_zip(zip_path, extract_to):
    """解压zip文件到指定目录"""
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            # 检查zip文件是否有效
            if zip_ref.testzip() is not None:
                return False, "ZIP文件已损坏"
            
            # 解压所有文件
            zip_ref.extractall(extract_to)
            return True, "解压成功"
    except zipfile.BadZipFile:
        return False, "无效的ZIP文件"
    except Exception as e:
        return False, f"解压失败: {str(e)}"


@app.route('/')
def index():
    """主页面"""
    return render_template('index.html')


@app.route('/api/projects', methods=['GET'])
def list_projects():
    """列出所有已部署的项目"""
    try:
        projects = []
        if os.path.exists(NGINX_ROOT):
            for item in os.listdir(NGINX_ROOT):
                item_path = os.path.join(NGINX_ROOT, item)
                if os.path.isdir(item_path):
                    stat_info = os.stat(item_path)
                    projects.append({
                        'name': item,
                        'path': item_path,
                        'modified': datetime.fromtimestamp(stat_info.st_mtime).strftime('%Y-%m-%d %H:%M:%S'),
                        'url': f'/{item}/'
                    })
        
        projects.sort(key=lambda x: x['modified'], reverse=True)
        return jsonify({'success': True, 'projects': projects})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500


@app.route('/api/upload', methods=['POST'])
def upload_file():
    """处理文件上传和解压"""
    try:
        # 检查是否有文件
        if 'file' not in request.files:
            return jsonify({'success': False, 'message': '未选择文件'}), 400
        
        file = request.files['file']
        
        if file.filename == '':
            return jsonify({'success': False, 'message': '未选择文件'}), 400
        
        if not allowed_file(file.filename):
            return jsonify({'success': False, 'message': '只允许上传.zip文件'}), 400
        
        # 获取项目名称（可选）
        project_name = request.form.get('project_name', '').strip()
        
        # 保存上传的文件
        filename = secure_filename(file.filename)
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        temp_zip_path = os.path.join(app.config['UPLOAD_FOLDER'], f'{timestamp}_{filename}')
        file.save(temp_zip_path)
        
        # 确定解压目标目录
        if project_name:
            # 使用指定的项目名称
            extract_dir = os.path.join(NGINX_ROOT, secure_filename(project_name))
        else:
            # 使用zip文件名（去掉.zip后缀）
            base_name = os.path.splitext(filename)[0]
            extract_dir = os.path.join(NGINX_ROOT, base_name)
        
        # 如果目录已存在，先备份
        if os.path.exists(extract_dir):
            backup_dir = f"{extract_dir}_backup_{timestamp}"
            shutil.move(extract_dir, backup_dir)
            backup_message = f"原目录已备份至: {os.path.basename(backup_dir)}"
        else:
            backup_message = None
        
        # 创建目标目录
        os.makedirs(extract_dir, exist_ok=True)
        
        # 解压文件
        success, message = extract_zip(temp_zip_path, extract_dir)
        
        # 删除临时zip文件
        os.remove(temp_zip_path)
        
        if success:
            project_url = f"/{os.path.basename(extract_dir)}/"
            response_data = {
                'success': True,
                'message': '上传并解压成功',
                'project_name': os.path.basename(extract_dir),
                'project_url': project_url,
                'extract_path': extract_dir
            }
            if backup_message:
                response_data['backup_message'] = backup_message
            
            return jsonify(response_data)
        else:
            # 解压失败，清理目录
            if os.path.exists(extract_dir):
                shutil.rmtree(extract_dir)
            return jsonify({'success': False, 'message': message}), 500
            
    except Exception as e:
        return jsonify({'success': False, 'message': f'处理失败: {str(e)}'}), 500


@app.route('/api/delete/<project_name>', methods=['DELETE'])
def delete_project(project_name):
    """删除项目"""
    try:
        project_path = os.path.join(NGINX_ROOT, secure_filename(project_name))
        
        if not os.path.exists(project_path):
            return jsonify({'success': False, 'message': '项目不存在'}), 404
        
        if not os.path.isdir(project_path):
            return jsonify({'success': False, 'message': '无效的项目路径'}), 400
        
        # 删除项目目录
        shutil.rmtree(project_path)
        
        return jsonify({'success': True, 'message': '项目已删除'})
    except Exception as e:
        return jsonify({'success': False, 'message': f'删除失败: {str(e)}'}), 500


if __name__ == '__main__':
    print("=" * 60)
    print("HTML原型文件上传工具启动")
    print(f"上传目录: {UPLOAD_FOLDER}")
    print(f"Nginx目录: {NGINX_ROOT}")
    print(f"访问地址: http://0.0.0.0:5000")
    print("=" * 60)
    
    # 开发环境使用，生产环境请使用gunicorn等WSGI服务器
    app.run(host='0.0.0.0', port=5000, debug=True)
