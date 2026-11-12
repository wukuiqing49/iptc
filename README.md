# CaptionMeta 官网

网站源页面与内部产品资料保留在仓库中。**只预览、上传或部署 `public/`**，不要把仓库根目录设为发布目录。

## 构建与预览

```powershell
python -m pip install -r app-launch-system/requirements.txt
python -B app-launch-system/scripts/launch.py build-site
python -B -m http.server 8000 --bind 127.0.0.1 --directory public
```

打开 http://127.0.0.1:8000/ 。`wrangler.toml` 的 Pages 输出目录已设置为 `public`。若使用 Cloudflare Git 集成，构建命令使用前两条，输出目录填 `public`。目录调整需要在下一次部署时生效；本地构建不会修改现有线上站点或提交搜索引擎索引请求。

## 内容与素材

- `site/content.py`：中文、英文首页和四篇任务指南，含功能边界与示例说明。
- `site/assets/`：审核过的真实应用截图、29 秒录屏、真实视频封面、分享图与样式/交互。
- `site/source-pages.json`：沿用的页面路由及验证文件。原页面保留为源输入，构建时定向优化，不覆盖源页面中的人工改动。
- `app-info.yaml`：产品版本、来源项目、正式商店与政策链接。Android 源项目不被修改。
- `.site-audit/`：公开文件清单、资源来源、生成哈希、审计和验证记录；不进入 `public`。

公开页面保留 11 种语言路由。中文与英文进入 sitemap；其余九种未经人工审核的翻译提供明确预览提示，使用 `noindex,follow`，不作为已审核页面的 hreflang 目标。审核后应同时更新页面状态、语言提示、hreflang 和 sitemap，而不是只删除提示。

隐私页直接链接 App 当前使用的正式隐私政策，不从依赖清单推导法律承诺。广告、应用内购买、文件格式差异和清理限制均在用户相关的位置说明。演示照片与署名不是客户案例。

## 更新与保护

修改 `site/` 源文件后再次运行 `build-site`。构建会检查引用、锚点、结构化数据和公开目录边界；如果 `public` 中的文件被人工修改或加入未知文件，构建会停止并保留原文件。先把人工修改合并回源文件，再重新构建。

如需从产品分析资料重建基础页面，原有 `generate-website --force` 命令仍可用；输出为本仓库时会自动接入 `build-site`。不要为普通文案更新重建全部基础页面。旧 `optimize_captionmeta_site.py` 已转为相同构建入口。

根目录与 `public` 的 Cloudflare Worker 均以公开路径白名单拦截内部材料。该防护需要部署后才在线上生效；实际发布仍以隔离的 `public` 为准。验证报告、哈希清单和源码证据不发布。

## 验证

```powershell
python -B -m unittest discover -s app-launch-system/tests -p test_official_site.py -v
python -B app-launch-system/scripts/launch.py validate-app-info app-info.yaml
```

浏览器还需检查首页、导航、语言切换、视频播放及失败状态、键盘焦点和移动端布局。静态检查通过不等于已上线或获得搜索排名。
