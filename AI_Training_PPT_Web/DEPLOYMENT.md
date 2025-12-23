# Cloudflare Pages 部署检查清单

## 推送前检查

- [ ] 已运行 `python3 tools/build.py` 或 `./build.sh` 验证构建成功
- [ ] `dist/` 目录包含以下文件:
  - [ ] `index.html`
  - [ ] `style.css`
  - [ ] `script.js`
  - [ ] `image/` 目录及其内容
- [ ] 已创建 `.gitignore` 文件
- [ ] 已添加 `wrangler.toml` 配置文件
- [ ] 已添加 `build.sh` 构建脚本

## GitHub 推送步骤

```bash
# 1. 初始化 Git 仓库 (如果还没有)
git init

# 2. 添加所有文件
git add .

# 3. 提交
git commit -m "Initial commit: AI Training PPT Web"

# 4. 添加远程仓库
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git

# 5. 推送到 GitHub
git push -u origin main
```

## Cloudflare Pages 部署步骤

### 方式 1: 自动配置 (推荐)

1. 登录 [Cloudflare Dashboard](https://dash.cloudflare.com/)
2. 进入 **Pages** → **Create a project**
3. 选择 **Connect to Git**
4. 授权并选择你的 GitHub 仓库
5. Cloudflare 会自动读取 `wrangler.toml` 配置
6. 点击 **Save and Deploy**

### 方式 2: 手动配置

如果自动配置失败,在设置页面手动填写:

- **Project name**: `ai-training-ppt` (或自定义)
- **Production branch**: `main`
- **Framework preset**: `None`
- **Build command**: `python tools/build.py` 或 `./build.sh`
- **Build output directory**: `dist`
- **Root directory**: `/` (留空)

## 部署后验证

- [ ] 访问 Cloudflare 提供的 URL
- [ ] 检查首页是否正常加载
- [ ] 测试键盘导航 (→ / ←)
- [ ] 验证图片是否正常显示
- [ ] 检查所有章节是否完整

## 常见问题

### 问题 1: `Output directory "dist" not found`

**原因**: 构建命令未执行或执行失败

**解决**:
1. 检查 Cloudflare Pages 构建日志
2. 确认 Build command 已正确设置
3. 尝试使用 `python tools/build.py` 替代 `./build.sh`

### 问题 2: 图片无法显示

**原因**: `image/` 目录未被复制到 `dist/`

**解决**:
1. 本地运行 `python3 tools/build.py`
2. 检查 `dist/image/` 是否存在
3. 如果不存在,检查 `tools/build.py` 中的图片复制逻辑

### 问题 3: CSS 样式丢失

**原因**: CSS 合并失败

**解决**:
1. 检查 `src/styles/base.css` 是否存在
2. 检查 `src/styles/chapters/*.css` 是否完整
3. 本地运行构建脚本验证

## 自定义域名 (可选)

1. 在 Cloudflare Pages 项目设置中
2. 进入 **Custom domains**
3. 添加你的域名
4. 按照提示配置 DNS 记录

---

**准备就绪后,即可推送到 GitHub 并部署!**
