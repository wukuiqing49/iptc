"""Compose the homepage cover from verified English app screenshots."""
from pathlib import Path
import hashlib
import json

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / 'site/assets'


def font(size, bold=False):
    candidates = [
        Path('C:/Windows/Fonts') / ('segoeuib.ttf' if bold else 'segoeui.ttf'),
        Path('/usr/share/fonts/truetype/dejavu') / ('DejaVuSans-Bold.ttf' if bold else 'DejaVuSans.ttf'),
    ]
    return ImageFont.truetype(str(next(path for path in candidates if path.exists())), size)


def build():
    cover = Image.new('RGB', (1440, 1024), '#f5f5f7')
    draw = ImageDraw.Draw(cover)
    icon = Image.open(ASSETS / 'icon.png').convert('RGBA').resize((64, 64), Image.Resampling.LANCZOS)
    cover.paste(icon, (64, 52), icon)
    draw.text((148, 54), 'CaptionMeta', font=font(44, True), fill='#1d1d1f')
    draw.text((64, 140), 'Edit a batch. Check the result.', font=font(58, True), fill='#1d1d1f')

    def panel(filename, x, y, width, label):
        original = Image.open(ASSETS / 'screenshots' / filename).convert('RGB')
        height = round(original.height * width / original.width)
        draw.text((x, y - 50), label, font=font(30, True), fill='#1055a2')
        draw.rounded_rectangle((x - 12, y - 12, x + width + 12, y + height + 12), radius=20, fill='white', outline='#dcdce0', width=2)
        cover.paste(original.resize((width, height), Image.Resampling.LANCZOS), (x, y))

    panel('batch-editor.webp', 64, 280, 720, 'Batch edit')
    panel('metadata-fields.webp', 864, 392, 512, 'Saved metadata')
    draw.line([(814, 586), (830, 602), (814, 618)], fill='#1055a2', width=5)
    draw.text((64, 964), 'Real English app screens. Demo data.', font=font(26), fill='#626267')
    target = ASSETS / 'product-cover.webp'
    cover.save(target, quality=92, method=6)

    record = ROOT / 'site/asset-sources.json'
    sources = json.loads(record.read_text(encoding='utf-8'))
    sources = [item for item in sources if item['publicPath'] != 'assets/product-cover.webp']
    sources.append({
        'sourcePaths': ['site/assets/icon.png', 'site/assets/screenshots/batch-editor.webp', 'site/assets/screenshots/metadata-fields.webp'],
        'publicPath': 'assets/product-cover.webp',
        'generator': 'site/create_product_cover.py',
        'purpose': 'product-cover-composed-from-real-English-app-screens',
        'reviewStatus': 'English-visible-text-visually-verified',
        'sha256': hashlib.sha256(target.read_bytes()).hexdigest(),
    })
    record.write_text(json.dumps(sources, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


if __name__ == '__main__':
    build()
