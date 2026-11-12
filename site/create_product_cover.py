"""使用项目宣传图的真实照片与英文结果界面，生成官网首屏封面。"""
from pathlib import Path
import hashlib
import json

from PIL import Image, ImageDraw, ImageOps

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / 'site/assets'


def build():
    cover = Image.new('RGB', (1440, 1200), '#f5f5f7')
    draw = ImageDraw.Draw(cover)

    def paste_rounded(source, box, radius):
        x, y, width, height = box
        image = ImageOps.fit(source.convert('RGB'), (width, height), Image.Resampling.LANCZOS)
        mask = Image.new('L', (width, height), 0)
        ImageDraw.Draw(mask).rounded_rectangle((0, 0, width - 1, height - 1), radius=radius, fill=255)
        cover.paste(image, (x, y), mask)

    # 与源项目 YouTube 封面相同的照片，保留人物和市场环境。
    photo = Image.open(ROOT / 'site/cover-sources/market-photo.png')
    paste_rounded(photo, (32, 48, 1096, 1080), 36)
    # 仅裁切真实界面，保留标题及说明、版权、署名、关键词，不重绘字段。
    result = Image.open(ASSETS / 'screenshots/metadata-result.webp').crop((0, 60, 540, 644))
    draw.rounded_rectangle((662, 300, 1418, 1120), radius=32, fill='#152a38')
    paste_rounded(result, (674, 312, 732, 796), 22)
    target = ASSETS / 'product-cover.webp'
    cover.save(target, quality=92, method=6)

    record = ROOT / 'site/asset-sources.json'
    sources = json.loads(record.read_text(encoding='utf-8'))
    sources = [item for item in sources if item['publicPath'] != 'assets/product-cover.webp']
    sources.append({
        'sourcePaths': ['site/cover-sources/market-photo.png', 'site/assets/screenshots/metadata-result.webp'],
        'photoOrigin': 'PressIPTC/docs/promo/20261109/sources/photo-preview.png',
        'photoCropPixels': [53, 353, 1027, 810],
        'interfaceCropPixels': [0, 60, 540, 644],
        'visualReference': 'PressIPTC/docs/promo/20261109/covers/youtube-main-landscape.jpg',
        'publicPath': 'assets/product-cover.webp',
        'generator': 'site/create_product_cover.py',
        'purpose': 'photography-scene-and-real-English-saved-metadata-cover',
        'reviewStatus': 'English-visible-text-visually-verified',
        'sha256': hashlib.sha256(target.read_bytes()).hexdigest(),
    })
    record.write_text(json.dumps(sources, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


if __name__ == '__main__':
    build()
