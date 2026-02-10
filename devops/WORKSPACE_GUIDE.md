# 工作空间功能使用指南

## 什么是工作空间？

工作空间（Workspace）是项目的分类容器，用于组织和管理不同类别的HTML原型项目。每个工作空间在文件系统中对应一个独立的目录。

### 使用场景

1. **按客户分类**
   - client-a（客户A的所有项目）
   - client-b（客户B的所有项目）
   - internal（内部项目）

2. **按项目类型分类**
   - prototypes（原型项目）
   - demos（演示项目）
   - archive（归档项目）

3. **按团队分类**
   - team-frontend（前端团队）
   - team-design（设计团队）
   - team-product（产品团队）

## 目录结构

```
工作空间根目录 (/usr/share/nginx/html)
│
├── client-a/                    ← 工作空间1
│   ├── homepage-v1/            ← 项目
│   ├── homepage-v2/            ← 项目
│   └── dashboard/              ← 项目
│
├── client-b/                    ← 工作空间2
│   ├── mobile-app/             ← 项目
│   └── website/                ← 项目
│
└── internal/                    ← 工作空间3
    ├── prototype-2024/         ← 项目
    └── test-project/           ← 项目
```

## 访问路径

项目访问路径格式：`http://server/工作空间名/项目名/`

### 示例

| 工作空间 | 项目名 | 访问URL |
|---------|--------|---------|
| client-a | homepage-v1 | http://server/client-a/homepage-v1/ |
| client-b | mobile-app | http://server/client-b/mobile-app/ |
| internal | prototype-2024 | http://server/internal/prototype-2024/ |

## 功能操作

### 1. 创建工作空间

**步骤：**
1. 点击左侧工作空间面板的 `+` 按钮
2. 在弹出的对话框中输入工作空间名称
3. 点击"创建"按钮

**命名建议：**
- 使用英文字母、数字、连字符
- 推荐格式：`client-a`, `team-design`, `project-2024`
- 避免使用空格和特殊字符
- 保持简短有意义

**示例：**
```
✅ 推荐：
- client-alibaba
- team-frontend
- archive-2024

❌ 不推荐：
- Client Alibaba（包含空格）
- 客户阿里（中文可用但不推荐）
- @client#1（特殊字符）
```

### 2. 选择工作空间

**步骤：**
1. 在左侧工作空间列表中点击工作空间名称
2. 选中的工作空间会高亮显示
3. 上传区域显示当前工作空间名称

**效果：**
- 上传区域变为可用状态
- 项目列表显示该工作空间的项目
- 后续上传的文件会解压到此工作空间

### 3. 上传到工作空间

**步骤：**
1. 先选择目标工作空间
2. 拖拽或选择ZIP文件
3. （可选）输入项目名称
4. 点击"上传并解压"

**结果：**
- 文件解压到：`工作空间目录/项目名/`
- 访问地址：`http://server/工作空间名/项目名/`

### 4. 查看工作空间项目

**当前工作空间：**
- 选择工作空间后，项目列表自动显示该工作空间的项目
- 每个项目卡片显示所属工作空间

**所有工作空间：**
- 刷新按钮可更新项目列表
- 项目卡片上显示所属工作空间标签

### 5. 删除工作空间

**步骤：**
1. 鼠标悬停在工作空间项上
2. 点击右侧出现的 🗑️ 图标
3. 确认删除

**限制：**
- ⚠️ 只能删除空的工作空间
- 如果工作空间包含项目，需要先删除所有项目
- 删除操作不可恢复

**清空工作空间步骤：**
1. 选择要删除的工作空间
2. 删除该工作空间下的所有项目
3. 返回删除空工作空间

## 最佳实践

### 1. 工作空间命名规范

建议建立统一的命名规范：

```
格式1: 按客户
- client-{客户代号}
  例如: client-abc, client-xyz

格式2: 按项目
- project-{项目名}
  例如: project-alpha, project-beta

格式3: 按时间
- archive-{年份}
  例如: archive-2024, archive-2025

格式4: 按团队
- team-{团队名}
  例如: team-frontend, team-design
```

### 2. 项目组织策略

**客户项目分离：**
```
client-a/
├── homepage/
├── mobile-app/
└── admin-panel/

client-b/
├── website/
└── dashboard/

internal/
└── test-projects/
```

**版本管理：**
```
client-a/
├── homepage-v1/
├── homepage-v2/
├── homepage-v3/
└── homepage-latest/
```

**开发阶段管理：**
```
project-alpha/
├── design-draft/
├── prototype/
├── final-demo/
└── production/
```

### 3. 权限建议

虽然当前版本不包含权限控制，但建议：

1. **生产环境**：通过nginx配置限制访问
2. **内网使用**：只在可信网络中部署
3. **敏感项目**：使用独立的工作空间

### 4. 维护建议

**定期清理：**
- 每季度检查并删除过期项目
- 将不再使用的项目移至归档工作空间
- 保持工作空间结构清晰

**备份策略：**
```bash
# 备份整个工作空间
tar -czf client-a-backup-$(date +%Y%m%d).tar.gz /path/to/workspace/client-a/

# 恢复工作空间
tar -xzf client-a-backup-20240210.tar.gz -C /path/to/workspace/
```

## 实际案例

### 案例1: 设计公司多客户管理

```
工作空间结构:
├── client-nike/
│   ├── campaign-2024/
│   └── product-showcase/
├── client-adidas/
│   ├── homepage-redesign/
│   └── mobile-first/
└── proposals/
    ├── pitch-nike/
    └── pitch-adidas/
```

**优势：**
- 客户项目隔离
- 便于权限管理
- 清晰的项目归属

### 案例2: 产品团队敏捷开发

```
工作空间结构:
├── sprint-01/
│   ├── feature-login/
│   └── feature-dashboard/
├── sprint-02/
│   ├── feature-reports/
│   └── feature-settings/
└── archive/
    └── old-prototypes/
```

**优势：**
- 按开发周期组织
- 便于版本追踪
- 自动归档旧版本

### 案例3: 前端团队组件库

```
工作空间结构:
├── components/
│   ├── buttons/
│   ├── forms/
│   └── navigation/
├── templates/
│   ├── dashboard/
│   └── landing-page/
└── demos/
    └── showcase/
```

**优势：**
- 资源分类清晰
- 便于团队协作
- 易于查找和复用

## 常见问题

### Q1: 工作空间和项目有什么区别？

**工作空间**：
- 一级目录，用于分类
- 相当于文件夹
- 一个工作空间可包含多个项目

**项目**：
- 二级目录，实际的HTML原型
- 相当于文件夹中的文件
- 每个项目是一个独立的网站

### Q2: 可以创建多少个工作空间？

没有数量限制，但建议：
- 保持在10-20个以内
- 过多会影响管理效率
- 定期清理不用的工作空间

### Q3: 能否移动项目到其他工作空间？

当前版本不支持直接移动，但可以：
1. 下载项目源文件
2. 重新上传到目标工作空间
3. 删除原项目

或通过文件系统操作：
```bash
mv /path/workspace/old-ws/project /path/workspace/new-ws/
```

### Q4: 删除工作空间会删除项目吗？

- 不会，只能删除**空**工作空间
- 必须先删除所有项目
- 这是为了防止误删除

### Q5: 工作空间名称可以修改吗？

当前版本不支持重命名，但可以：
1. 创建新工作空间
2. 将项目重新上传到新工作空间
3. 删除旧工作空间

或通过文件系统操作：
```bash
mv /path/workspace/old-name /path/workspace/new-name
```
然后刷新页面

## 技巧与提示

💡 **提示1**: 为每个客户创建独立工作空间，便于管理和权限控制

💡 **提示2**: 使用有意义的工作空间名称，如 `client-{客户名}`

💡 **提示3**: 定期将过期项目移至 `archive` 工作空间

💡 **提示4**: 工作空间列表显示项目数量，便于了解使用情况

💡 **提示5**: 选中工作空间会在上传区域顶部显示，避免上传错误

## 总结

工作空间功能帮助你：
- ✅ 更好地组织项目
- ✅ 清晰的分类管理
- ✅ 便于团队协作
- ✅ 提高工作效率

合理使用工作空间，让你的HTML原型管理更加井井有条！
