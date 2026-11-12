# CaptionMeta 官网维护入口

完整流程见项目根目录 [README](../README.md)。在项目根目录运行：

```powershell
python -m pip install -r app-launch-system/requirements.txt
python -B app-launch-system/scripts/launch.py build-site
```

当前正式输出为 `public/`。旧优化脚本已委托给此构建流程，不再直接批量修改源 HTML。构建清单自动包含全部图标及审核过的媒体资源，并保护已有人工修改。

Cloudflare 当前没有构建命令，因此 `public/` 必须纳入 Git，与源文件和 `site/public-manifest.json` 一起提交。自动部署直接发布预构建产物，不依赖 Cloudflare 安装 Python。不要重新忽略 `public/`，否则部署会报输出目录不存在。

只部署 `public/`；不要上传 `.site-audit/`、源码、模板或分析配置。运行后检查桌面、移动端首页和视频播放，再发布静态文件。脚本不部署、不提交搜索引擎索引请求。
