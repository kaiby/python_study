# 备份策略对比

本文档详细对比 `AUTO_BACKUP` 配置的两种模式。

## 快速对比

| 特性 | 备份模式 (True) | 覆盖模式 (False) |
|------|----------------|-----------------|
| **配置值** | `AUTO_BACKUP = True` | `AUTO_BACKUP = False` |
| **同名处理** | 重命名为 `xxx_backup_时间戳` | 直接删除 |
| **历史版本** | ✅ 保留所有版本 | ❌ 不保留 |
| **磁盘占用** | ⚠️ 较高 | ✅ 最小 |
| **可恢复性** | ✅ 可回滚 | ❌ 不可恢复 |
| **维护成本** | ⚠️ 需定期清理备份 | ✅ 无需维护 |
| **推荐场景** | 生产、客户项目 | 开发、测试环境 |

## 详细说明

### 备份模式 (AUTO_BACKUP = True)

#### 工作流程

```
步骤1: 上传 project.zip
└─> 检查 /workspace/client-a/project/ 是否存在

步骤2: 如果存在
└─> 重命名为 /workspace/client-a/project_backup_20240210_143520/

步骤3: 解压新文件
└─> 创建 /workspace/client-a/project/

步骤4: 完成
├─> /workspace/client-a/project/  (新版本)
└─> /workspace/client-a/project_backup_20240210_143520/  (旧版本)
```

#### 目录结构演变

**第一次上传**:
```
workspace/
└── client-a/
    └── homepage/
        ├── index.html
        └── css/
```

**第二次上传（更新）**:
```
workspace/
└── client-a/
    ├── homepage/                              ← 新版本
    │   ├── index.html
    │   └── css/
    └── homepage_backup_20240210_143520/       ← 第一版备份
        ├── index.html
        └── css/
```

**第三次上传（再次更新）**:
```
workspace/
└── client-a/
    ├── homepage/                              ← 最新版本
    │   ├── index.html
    │   └── css/
    ├── homepage_backup_20240210_143520/       ← 第一版备份
    │   ├── index.html
    │   └── css/
    └── homepage_backup_20240210_153022/       ← 第二版备份
        ├── index.html
        └── css/
```

#### 优势

1. **安全可靠**
   - 任何更新都不会丢失数据
   - 可以随时回滚到任何历史版本
   - 适合重要的生产项目

2. **便于对比**
   - 可以对比新旧版本
   - 方便客户确认变更
   - 便于问题追溯

3. **灾难恢复**
   - 误上传可以恢复
   - 出错可以快速回滚
   - 降低操作风险

#### 劣势

1. **磁盘空间**
   - 每次更新都会保留旧版本
   - 长期使用会占用大量空间
   - 需要定期清理

2. **管理成本**
   - 需要手动清理备份
   - 目录结构变复杂
   - 可能混淆版本

3. **访问问题**
   - 备份文件夹也会在列表中显示
   - 需要注意区分当前版本和备份

#### 清理备份的方法

**手动清理**:
```bash
# 查看备份文件
ls -la /workspace/client-a/ | grep backup

# 删除特定备份
rm -rf /workspace/client-a/homepage_backup_20240210_143520

# 删除所有7天前的备份
find /workspace -name "*_backup_*" -mtime +7 -type d -exec rm -rf {} \;
```

**自动清理脚本**:
```bash
#!/bin/bash
# cleanup-backups.sh
# 删除超过30天的备份文件

WORKSPACE_ROOT="/usr/share/nginx/html"
DAYS=30

find "$WORKSPACE_ROOT" -name "*_backup_*" -type d -mtime +$DAYS -exec rm -rf {} \;
echo "已清理${DAYS}天前的备份"
```

**定时任务**:
```bash
# 每周日凌晨2点清理
(crontab -l 2>/dev/null; echo "0 2 * * 0 /usr/local/bin/cleanup-backups.sh") | crontab -
```

### 覆盖模式 (AUTO_BACKUP = False)

#### 工作流程

```
步骤1: 上传 project.zip
└─> 检查 /workspace/client-a/project/ 是否存在

步骤2: 如果存在
└─> 删除 /workspace/client-a/project/

步骤3: 解压新文件
└─> 创建 /workspace/client-a/project/

步骤4: 完成
└─> /workspace/client-a/project/  (新版本，旧版本已删除)
```

#### 目录结构演变

**第一次上传**:
```
workspace/
└── client-a/
    └── homepage/
        ├── index.html
        └── css/
```

**第二次上传（更新）**:
```
workspace/
└── client-a/
    └── homepage/          ← 新版本，旧版本已被删除
        ├── index.html
        └── css/
```

**第三次上传（再次更新）**:
```
workspace/
└── client-a/
    └── homepage/          ← 最新版本，历史版本全部被删除
        ├── index.html
        └── css/
```

#### 优势

1. **节省空间**
   - 不保留历史版本
   - 磁盘占用最小化
   - 适合频繁更新

2. **目录简洁**
   - 只保留最新版本
   - 目录结构清晰
   - 易于管理

3. **无需维护**
   - 不需要清理备份
   - 自动管理空间
   - 降低维护成本

#### 劣势

1. **不可恢复**
   - 覆盖后无法回滚
   - 误操作无法撤销
   - 需要额外的版本控制

2. **风险较高**
   - 上传错误文件无法恢复
   - 数据丢失风险
   - 不适合生产环境

3. **无法对比**
   - 无法查看历史版本
   - 不能对比变更
   - 问题追溯困难

#### 风险控制建议

如果使用覆盖模式，建议：

1. **使用外部版本控制**:
```bash
# 在上传前先备份到Git
cd /workspace/client-a/homepage
git add .
git commit -m "Backup before update"
git push
```

2. **定期整体备份**:
```bash
# 每天备份整个工作空间
tar -czf workspace-backup-$(date +%Y%m%d).tar.gz /workspace
```

3. **重要项目使用备份模式**:
```python
# 根据工作空间决定是否备份
if workspace_name in ['production', 'client-important']:
    AUTO_BACKUP = True
else:
    AUTO_BACKUP = False
```

## 使用场景推荐

### 推荐使用备份模式的场景

1. **客户项目**
   - 需要展示给客户的原型
   - 需要客户确认的设计稿
   - 客户可能要求查看历史版本

2. **生产环境**
   - 正式上线的项目
   - 需要审批的内容
   - 关键业务原型

3. **长期维护项目**
   - 持续迭代的项目
   - 需要版本对比的项目
   - 可能需要回滚的项目

4. **团队协作**
   - 多人参与的项目
   - 需要版本追溯的项目
   - 需要审查变更的项目

### 推荐使用覆盖模式的场景

1. **开发环境**
   - 快速迭代的原型
   - 实验性项目
   - 临时测试

2. **个人项目**
   - 个人练习项目
   - 一次性演示
   - 不需要历史记录

3. **资源受限**
   - 磁盘空间有限
   - 需要频繁更新
   - 已有其他版本控制

4. **临时文件**
   - 演示用的临时文件
   - 快速原型验证
   - 短期使用的项目

## 混合策略

如果需要更灵活的策略，可以修改代码实现：

### 方案1: 按工作空间区分

```python
# 重要客户使用备份模式，测试环境使用覆盖模式
IMPORTANT_WORKSPACES = ['client-vip', 'production', 'important']

def should_backup(workspace_name):
    return workspace_name in IMPORTANT_WORKSPACES or AUTO_BACKUP
```

### 方案2: 按项目名称区分

```python
# production/release 开头的项目强制备份
def should_backup(project_name):
    if project_name.startswith(('production', 'release', 'v')):
        return True
    return AUTO_BACKUP
```

### 方案3: 限制备份数量

```python
# 最多保留3个备份，超过则删除最旧的
MAX_BACKUPS = 3

def cleanup_old_backups(project_path):
    backups = sorted([d for d in os.listdir(os.path.dirname(project_path)) 
                     if d.startswith(os.path.basename(project_path) + '_backup_')])
    while len(backups) > MAX_BACKUPS:
        oldest = backups.pop(0)
        shutil.rmtree(os.path.join(os.path.dirname(project_path), oldest))
```

## 配置建议总结

### 保守策略（推荐新手）
```python
AUTO_BACKUP = True
```
- 安全第一
- 容错率高
- 适合生产环境

### 激进策略（适合有经验用户）
```python
AUTO_BACKUP = False
```
- 性能优先
- 节省空间
- 适合开发环境

### 平衡策略（推荐）
```python
# 根据实际情况选择
# 生产环境: True
# 开发环境: False
# 或使用混合策略
```

## 总结

选择合适的备份策略需要考虑：

1. **项目重要性** - 重要项目使用备份模式
2. **更新频率** - 频繁更新考虑覆盖模式
3. **磁盘空间** - 空间有限考虑覆盖模式
4. **团队规模** - 团队协作推荐备份模式
5. **版本控制** - 已有Git等工具可用覆盖模式

**建议**:
- 生产环境：`AUTO_BACKUP = True`
- 开发环境：`AUTO_BACKUP = False`
- 根据实际需求灵活调整

记住：**没有最好的策略，只有最适合的策略**！
