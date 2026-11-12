"""构建 CaptionMeta 可部署官网；公开产物与内部记录严格分离。"""
from __future__ import annotations

import argparse
import hashlib
import html
import json
import shutil
import sys
import tempfile
from pathlib import Path
from urllib.parse import unquote, urlsplit, urljoin
import xml.etree.ElementTree as ET

from bs4 import BeautifulSoup
from PIL import Image
import yaml

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'site'))
from content import COPY, GUIDES

SITE = 'https://iptc.pages.dev'
PLAY = 'https://play.google.com/store/apps/details?id=com.wkq.caption'
POLICY = 'https://wukuiqing49.github.io/agreement/cm_privacy_policy.html'
PRIMARY = {'zh-CN', 'en-US'}
DAY = '2026-11-12'
AUDIT = ROOT / '.site-audit'
VIDEO = '/assets/video/captionmeta-batch.mp4'
THUMBNAIL = '/assets/video-poster.webp'


def watch_path(locale):
    return ('/en-US' if locale == 'en-US' else '') + '/watch/batch-editing/'


def render_watch(locale):
    c = COPY[locale]
    zh = locale == 'zh-CN'
    home = '/' if zh else '/en-US/'
    title = c['videoLabel'] + ' · 29 ' + ('秒' if zh else 'seconds')
    canonical = SITE + watch_path(locale)
    transcript = esc(c['transcriptText'])
    return f'''<!doctype html>
<html lang="{locale}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)} | CaptionMeta</title><meta name="description" content="{esc(c['videoCopy'])}">
<meta name="robots" content="index,follow,max-image-preview:large,max-video-preview:-1">
<link rel="canonical" href="{canonical}">
<link rel="alternate" hreflang="zh-CN" href="{SITE}{watch_path('zh-CN')}">
<link rel="alternate" hreflang="en-US" href="{SITE}{watch_path('en-US')}">
<link rel="alternate" hreflang="x-default" href="{SITE}{watch_path('zh-CN')}">
<meta property="og:type" content="video.other"><meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(c['videoCopy'])}"><meta property="og:url" content="{canonical}">
<meta property="og:image" content="{SITE}{THUMBNAIL}"><meta property="og:image:width" content="540"><meta property="og:image:height" content="960">
<meta property="og:video" content="{SITE}{VIDEO}"><meta property="og:video:type" content="video/mp4">
<meta property="og:video:width" content="1080"><meta property="og:video:height" content="1920">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:image" content="{SITE}{THUMBNAIL}">
<link rel="icon" href="/favicon.ico"><link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
<link rel="stylesheet" href="/assets/styles.css"><link rel="stylesheet" href="/assets/refinements.css">
</head><body><a class="skip-link" href="#main">{'跳至视频' if zh else 'Skip to video'}</a>
<header class="site-header"><a class="brand" href="{home}"><img src="/assets/icon.png" alt="" width="40" height="40"><span>CaptionMeta</span></a>
<button class="nav-toggle" type="button" aria-controls="primary-navigation" aria-expanded="false">{'菜单' if zh else 'Menu'}</button>
<nav id="primary-navigation" aria-label="{'导航' if zh else 'Navigation'}"><a href="{home}">{'产品首页' if zh else 'Product home'}</a><a href="{watch_path('en-US' if zh else 'zh-CN')}" lang="{'en-US' if zh else 'zh-CN'}">{'English' if zh else '中文'}</a></nav></header>
<main id="main" class="watch-page"><h1>{esc(title)}</h1>
<figure class="watch-player"><video controls playsinline preload="metadata" poster="{THUMBNAIL}" width="1080" height="1920" aria-label="{esc(c['videoLabel'])}"><source src="{VIDEO}" type="video/mp4"><a href="{VIDEO}">{esc(c['videoLink'])}</a></video><p class="video-error" role="status" hidden>{esc(c['videoFallback'])}</p></figure>
<p>{esc(c['videoCopy'])}</p><p><a href="{VIDEO}">{esc(c['videoLink'])}</a></p>
<section class="watch-transcript"><h2>{esc(c['transcript'])}</h2><p>{transcript}</p></section>
<p><a href="{home}#screenshots">{esc(c['screensTitle'])}</a></p>{action(c)}
</main><footer><p>CaptionMeta · <a href="{home}support.html">{'帮助与支持' if zh else 'Help and support'}</a></p></footer>
<script src="/assets/app.js" defer></script></body></html>'''


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def esc(value):
    return html.escape(str(value), quote=True)


def fragment(markup):
    return BeautifulSoup(markup, 'html.parser')


def replace_contents(tag, markup):
    tag.clear()
    tag.append(fragment(markup))


def action(c, prefix=''):
    return f'<a class="primary-action store-action" href="{PLAY}"><img src="/assets/google-play-badge.png" alt="{esc(c["download"])}" width="646" height="250"></a>'


def image(name, caption, prefix, eager=False):
    width, height = Image.open(ROOT / 'site/assets/screenshots' / name).size
    return (f'<img src="{prefix}assets/screenshots/{name}" alt="{esc(caption)}" '
            f'width="{width}" height="{height}" loading="{"eager" if eager else "lazy"}" decoding="async">')


def render_home(c, locale, locale_data, links, prefix):
    zh = locale == 'zh-CN'
    zoom = '放大英文界面' if zh else 'Enlarge the English interface'
    crop = '真实英文界面局部 · 演示数据' if zh else 'Actual English interface detail · demo data'
    items = [
        ('batch-editor.webp', 'metadata-editor', '一组照片，一次填写' if zh else 'One edit. A whole batch.', c['captions'][0]),
        ('presets.webp', 'batch-presets', '把常用字段留给下次' if zh else 'Keep your setup for next time.', c['captions'][1]),
        ('metadata-result.webp', 'metadata-editor', '保存以后，再检查一次' if zh else 'See what made it into the file.', c['captions'][2]),
        ('privacy-result.webp', 'privacy-cleanup', '分享之前，检查隐私信息' if zh else 'Check the details before sharing.', c['captions'][3]),
    ]
    cards = ''.join(f'''<article class="showcase-card"><div class="showcase-copy"><h3>{esc(title)}</h3><p>{esc(body)}</p><a class="feature-link" href="{esc(links[fid])}">{esc(c['details'])}</a></div><figure><a class="screen-zoom" href="{prefix}assets/screenshots/{name}" aria-label="{esc(zoom)}: {esc(title)}">{image(name, title, prefix)}<span>{esc(zoom)}</span></a><figcaption>{esc(crop)}</figcaption></figure></article>''' for name, fid, title, body in items)
    faq = ''.join(f'<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>' for q, a in c['faq'])
    return f'''
    <section class="hero home-hero" aria-labelledby="hero-title">
      <div class="hero-copy"><p class="platform">{esc(c['platform'])}</p>
        <h1 id="hero-title">{esc(c['headline']).replace(chr(10), '<br>')}</h1>
        <p class="summary">{esc(c['intro'])}</p>
        <div class="hero-actions">{action(c)}<a class="secondary-action" href="{watch_path(locale)}">{esc(c['secondary'])}</a></div>
        <p class="store-note">{esc(c['store'])}</p>
      </div>
      <figure class="hero-media editor-media"><a class="screen-zoom" href="{prefix}assets/screenshots/batch-editor.webp" aria-label="{esc(zoom)}">{image('batch-editor.webp', c['screenNames'][0], prefix, True)}</a><figcaption>{esc(crop)}</figcaption></figure>
    </section>
    <section class="workflow compact-workflow" aria-label="{esc(c['workflowTitle'])}"><ol>{''.join('<li>'+esc(s)+'</li>' for s in (['选择照片', '填写或应用预设', '保存并检查结果', '分享或交付'] if zh else ['Choose photos', 'Fill fields or apply a preset', 'Save and check the result', 'Share or deliver']))}</ol></section>
    <section id="features" class="content-band showcase-band"><div id="screenshots" class="section-heading"><h2>{esc(c['featuresTitle'])}</h2><p>{esc(c['screensIntro'])}</p></div><div class="showcase-grid">{cards}</div><p class="delivery-note"><a href="{esc(links['photo-delivery'])}">{'需要发送到自己的服务器？了解照片交付队列。' if zh else 'Sending to your own server? Explore the photo delivery queue.'}</a></p></section>
    <section id="walkthrough" class="walkthrough"><div class="walkthrough-copy"><h2>{esc(c['videoTitle'])}</h2><p>{esc(c['videoCopy'])}</p><a class="secondary-action" href="{watch_path(locale)}">{'观看 29 秒演示' if zh else 'Watch the 29-second demo'}</a></div><a class="demo-preview" href="{watch_path(locale)}" aria-label="{esc(c['videoLabel'])}"><img src="{prefix}assets/video-poster.webp" width="540" height="960" alt="{esc(c['videoLabel'])}" loading="lazy"><span aria-hidden="true">▶ 0:29</span></a></section>
    <section class="site-faq"><h2>{esc(c['faqTitle'])}</h2>{faq}</section>
    <section class="closing"><h2>{esc(c['closing'])}</h2>{action(c)}<p class="store-note">{esc(c['store'])}</p></section>'''


def render_guide(c, data, locale, prefix, feature_url, fid):
    sections = ''.join(f'<section id="step-{i}"><h2>{esc(title)}</h2>{body}</section>' for i, (title, body) in enumerate(data['sections'], 1))
    toc = ''.join(f'<a href="#step-{i}">{esc(title)}</a>' for i, (title, _) in enumerate(data['sections'], 1))
    home = '/' if locale == 'zh-CN' else '/en-US/'
    guide_home = '/blog/' if locale == 'zh-CN' else '/blog/en-US/'
    home_name, guide_name = ('首页', '指南') if locale == 'zh-CN' else ('Home', 'Guides')
    return f'''<article><header class="article-header"><nav class="breadcrumbs" aria-label="Breadcrumb"><a href="{home}">{home_name}</a><span>/</span><a href="{guide_home}">{guide_name}</a></nav><p class="article-kicker">{esc(c['guideLabel'])}</p><h1>{esc(data['title'])}</h1><p class="article-dek">{esc(data['intro'])}</p><p class="article-meta">{esc(c['version'])} · <time datetime="{DAY}">{DAY}</time></p></header><div class="article-layout"><aside class="article-toc"><nav>{toc}</nav></aside><div class="article-body">{sections}<figure class="guide-screen"><a class="screen-zoom" href="{prefix}assets/screenshots/{GUIDES[fid]['image']}">{image(GUIDES[fid]['image'], data['title'], prefix)}</a><figcaption>{esc(c['screensIntro'])}</figcaption></figure><p><a href="{feature_url}">{esc(c['details'])}</a></p>{action(c)}</div></div></article>'''


def metadata(soup, locale, canonical, title, description, prefix, primary, version):
    soup.title.string = title
    description_tag = soup.find('meta', attrs={'name': 'description'})
    if description_tag:
        description_tag['content'] = description
    for tag in soup.head.find_all('meta'):
        key = tag.get('property', tag.get('name', ''))
        if key.startswith(('og:', 'twitter:')) or key == 'robots':
            tag.decompose()
    for tag in list(soup.head.find_all('link')):
        if 'icon' in ' '.join(tag.get('rel', [])):
            tag.decompose()
        elif 'alternate' in tag.get('rel', []):
            if not primary or tag.get('hreflang') not in PRIMARY | {'x-default'}:
                tag.decompose()
    tags = {'robots': 'index,follow,max-image-preview:large' if primary else 'noindex,follow',
            'og:type': 'website', 'og:title': title, 'og:description': description,
            'og:url': canonical, 'og:site_name': 'CaptionMeta', 'og:image': SITE + '/assets/social-card.jpg',
            'og:image:width': '1200', 'og:image:height': '630', 'og:image:alt': 'CaptionMeta photo metadata editor',
            'twitter:card': 'summary_large_image', 'twitter:title': title, 'twitter:description': description,
            'twitter:image': SITE + '/assets/social-card.jpg'}
    for name, value in tags.items():
        tag = soup.new_tag('meta', attrs={('property' if name.startswith('og:') else 'name'): name, 'content': value})
        soup.head.append(tag)
    for rel, url, size, mime in [('icon', 'favicon.ico', '16x16 32x32 48x48', 'image/x-icon'), ('icon', 'assets/favicon.png', '96x96', 'image/png'), ('apple-touch-icon', 'assets/apple-touch-icon.png', '180x180', 'image/png')]:
        soup.head.append(soup.new_tag('link', attrs={'rel': rel, 'href': prefix + url, 'sizes': size, 'type': mime}))
    for script in soup.select('script[type="application/ld+json"]'):
        data = json.loads(script.string or script.get_text())
        if data.get('@type') == 'WebSite' and locale != 'zh-CN':
            script.decompose()
            continue
        if data.get('@type') == 'SoftwareApplication':
            data.update(description=description, applicationCategory='MultimediaApplication', softwareVersion=version, publisher={'@type': 'Organization', 'name': '上海促动科技有限公司'})
        script.string = json.dumps(data, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')
    crumbs = soup.select('.breadcrumbs a')
    if primary and crumbs:
        items = [{'@type':'ListItem','position':i,'name':a.get_text(strip=True),'item':urljoin(canonical,a['href'])} for i,a in enumerate(crumbs,1)]
        items.append({'@type':'ListItem','position':len(items)+1,'name':soup.h1.get_text(strip=True),'item':canonical})
        tag = soup.new_tag('script', type='application/ld+json')
        tag.string = json.dumps({'@context':'https://schema.org','@type':'BreadcrumbList','itemListElement':items},ensure_ascii=False).replace('</','<\\/')
        soup.head.append(tag)


def transform(path, rel, locale_data, version):
    soup = BeautifulSoup(path.read_text(encoding='utf-8'), 'html.parser')
    if not soup.head or not soup.title:
        return False
    locale = soup.html.get('lang', 'zh-CN')
    primary = locale in PRIMARY
    c = dict(COPY.get(locale, COPY['en-US']))
    c['version'] = ('当前版本 ' if locale == 'zh-CN' else 'Current version ') + version
    base = locale_data.get(locale, locale_data['en-US'])
    prefix = '../' * (len(Path(rel).parts) - 1)
    canonical_tag = soup.find('link', rel='canonical')
    if not canonical_tag:
        return False
    canonical = canonical_tag['href']
    title = soup.title.get_text()
    description = soup.find('meta', attrs={'name': 'description'})['content']
    main = soup.find('main')
    for text_node in list(soup.find_all(string=lambda value: value and '1.2.5' in value)):
        text_node.replace_with(str(text_node).replace('1.2.5', version))
    home = soup.find(id='hero-title') is not None
    feature = soup.select_one('.feature-detail') is not None
    article = soup.select_one('.article-layout') is not None
    fid = None
    config_tag = soup.find('script', id='locale-routes')
    config = json.loads(config_tag.string) if config_tag else None
    # 按已有中文等价路由识别功能，避免按外语标题猜测。
    source_url = next((x['url'] for x in config['locales'] if x['code'] == 'zh-CN'), '') if config else ''
    for key in GUIDES:
        if key in source_url:
            fid = key
            break
    links = {}
    for a in soup.select('.feature-list .feature-link'):
        for key in GUIDES:
            if key in a.get('href', ''):
                links[key] = a['href']
    if home and primary:
        # 英文 slug 与中文不同，从实际特性顺序中提取已存在路由。
        links = {}
        for key in GUIDES:
            label = base['home']['features'][key]['name']
            card = next(card for card in soup.select('.feature-list article') if card.h3.get_text() == label)
            links[key] = card.select_one('a')['href']
        replace_contents(main, render_home(c, locale, base, links, prefix))
        title, description = c['title'], c['description']
    elif home:
        media = soup.select_one('.hero-media')
        if media:
            replace_contents(media, image('batch-editor.webp', base['home']['category'], prefix, True))
        shot_list = soup.select_one('.screenshot-list')
        if shot_list:
            replace_contents(shot_list, ''.join(f'<figure>{image(name, base["home"]["category"], prefix)}</figure>' for name in ['batch-editor.webp', 'presets.webp', 'metadata-result.webp']))
        for band in ['.screenshot-band', '.content-band']:
            intro = soup.select_one(band + ' .section-heading p')
            if intro:
                intro.decompose()
        close_p = soup.select_one('.closing p')
        if close_p:
            close_p.decompose()
        if not soup.select_one('.hero-copy .primary-action'):
            soup.select_one('.hero-copy').append(fragment(action(c)))
    if feature:
        for evidence in soup.select('.feature-evidence'):
            evidence.decompose()
        category = soup.select_one('.feature-hero .category')
        if category:
            category.decompose()
        media = soup.select_one('.feature-media')
        if media:
            shot = GUIDES[fid]['image'] if fid else 'batch-editor.webp'
            replace_contents(media, f'<a class="screen-zoom" href="{prefix}assets/screenshots/{shot}">{image(shot, title, prefix)}</a>' + f'<figcaption>{esc(c["screensIntro"])}</figcaption>')
        if primary:
            # 将实现口吻替换为用户说明，保留其余经核对的功能说明。
            for p in soup.select('.feature-faq p'):
                if fid == 'metadata-editor':
                    p.string = ('可以编辑支持的 IPTC 与 XMP 字段。具体可用字段取决于文件格式和工作流设置，请在保存后检查结果。' if locale == 'zh-CN' else 'You can edit supported IPTC and XMP fields. Available fields depend on the file format and workflow settings; check the generated file.')
                elif fid == 'photo-delivery':
                    p.string = ('可配置 FTP、FTPS、SFTP、HTTP、SMB 和 WebDAV。你需要自行提供服务器和有效凭据。' if locale == 'zh-CN' else 'Configure FTP, FTPS, SFTP, HTTP, SMB or WebDAV with your own server and valid credentials.')
            if fid == 'privacy-cleanup':
                soup.select_one('.feature-limitations').append(fragment('<p>' + esc(c['faq'][-1][1]) + '</p>'))
            soup.select_one('.feature-hero').append(fragment(action(c)))
    if article and primary and fid:
        related = soup.select_one('.related-band')
        guide_feature = next((a['href'] for a in soup.select('a[href]') if '/features/' in a['href'] or a['href'].startswith('../../features/')), None)
        if not guide_feature:
            slug = {'metadata-editor':'iptc-exif-and-xmp-editing','privacy-cleanup':'private-metadata-cleanup','batch-presets':'batch-presets','photo-delivery':'photo-delivery-queue'}[fid] if locale == 'en-US' else fid
            guide_feature = ('/en-US/features/' if locale == 'en-US' else '/features/') + slug + '/'
        replace_contents(main, render_guide(c, GUIDES[fid][locale], locale, prefix, guide_feature, fid))
        if related:
            main.append(related)
        title, description = GUIDES[fid][locale]['title'] + ' | CaptionMeta', GUIDES[fid][locale]['intro']
    if primary and rel.endswith('support.html'):
        questions = ''.join(f'<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>' for q,a in c['supportQuestions'])
        replace_contents(main, f'<h1>{esc(c["supportTitle"])}</h1><p class="company-intro">{esc(c["supportIntro"])}</p><p>{esc(c["version"])} · {esc(c["platform"])}</p>{action(c)}<section><h2>{esc(c["faqTitle"])}</h2>{questions}</section><p><a href="mailto:wukuiqing@gmail.com">wukuiqing@gmail.com</a></p>')
        title, description = c['supportTitle'] + ' | CaptionMeta', c['supportIntro']
    elif rel.endswith('support.html'):
        answers = soup.select('main details p')
        if len(answers) >= 2:
            replace_contents(answers[1], f'<a href="{PLAY}">{esc(base["common"]["googlePlayCta"])}</a>')
    if rel.endswith('privacy.html'):
        # 使用 App 中已发布的政策链接，不根据源码编写法律承诺。
        heading = soup.h1.get_text()
        replace_contents(main, f'<h1>{esc(c["privacyTitle"] if primary else heading)}</h1><p>{esc(c["privacyIntro"])}</p><a class="primary-action" href="{POLICY}">{esc(c["privacyAction"])}</a><p>{esc(c["privacyMore"])}</p><p><a href="{PLAY}">Google Play · Data safety</a></p><p><a href="mailto:wukuiqing@gmail.com">wukuiqing@gmail.com</a></p>')
        if primary:
            title, description = c['privacyTitle'] + ' | CaptionMeta', c['privacyIntro']
    # 预览翻译不进入索引，也不作为已审核页面的 hreflang 目标。
    if not primary:
        notice = soup.new_tag('aside', attrs={'class': 'translation-notice', 'role': 'note'})
        notices = {'ja-JP':'翻訳プレビューです。内容は英語版または中国語版でご確認ください。', 'ko-KR':'번역 미리보기입니다. 자세한 내용은 영어 또는 중국어 페이지를 확인하세요.', 'de-DE':'Übersetzungsvorschau. Bitte prüfen Sie die Angaben auf Englisch oder Chinesisch.', 'fr-FR':'Aperçu de traduction. Consultez les informations en anglais ou en chinois.', 'es-419':'Vista previa de traducción. Consulta la información en inglés o chino.', 'pt-PT':'Pré-visualização da tradução. Consulte as informações em inglês ou chinês.', 'it-IT':'Anteprima della traduzione. Consulta le informazioni in inglese o cinese.', 'ru-RU':'Предварительный перевод. Сверьте сведения с английской или китайской версией.', 'ar':'معاينة للترجمة. يُرجى مراجعة المعلومات بالإنجليزية أو الصينية.'}
        notice.string = notices[locale] + ' '
        a = soup.new_tag('a', href='/en-US/'); a.string='English'; notice.append(a)
        main.insert_before(notice)
    if config:
        for item in config['locales']:
            item['url'] = urlsplit(item['url']).path
            if Path(item['url']).name in {'about','support','privacy'}:
                item['url'] += '.html'
        config_tag.string = json.dumps(config, ensure_ascii=False)
    # 让标准静态预览与 Pages 均可导航；canonical 仍保持已上线的干净 URL。
    for anchor in soup.select('a[href]'):
        url = urlsplit(anchor['href'])
        if not url.scheme and not url.netloc and Path(url.path).name in {'about','support','privacy'}:
            anchor['href'] = url.path + '.html' + ('?'+url.query if url.query else '') + ('#'+url.fragment if url.fragment else '')
    # 折叠菜单在无脚本时仍显示，键盘可操作。
    header = soup.select_one('header.site-header')
    if header and header.nav:
        nav = header.nav
        nav['id'] = 'primary-navigation'
        button = soup.new_tag('button', attrs={'class':'nav-toggle', 'type':'button', 'aria-controls':'primary-navigation', 'aria-expanded':'false'})
        button.string = '菜单' if locale == 'zh-CN' else 'Menu'
        nav.insert_before(button)
    # 所有页面均加载统一交互，含视频失败状态、焦点与导航。
    if not soup.find('script', src=prefix + 'assets/app.js'):
        soup.body.append(soup.new_tag('script', src=prefix + 'assets/app.js', defer=True))
    for img in soup.find_all('img'):
        src = img.get('src','')
        if src.endswith('02-captionmeta-upload.png'):
            img['src'] = prefix + 'assets/screenshots/metadata-result.webp'
            img['alt'] = c['screenNames'][2]
        if src.endswith('01-captionmeta-home.png'):
            img['src'] = prefix + 'assets/screenshots/batch-editor.webp'
            img['alt'] = c['screenNames'][0]
        if '/screenshots/' in img.get('src','') and not img['src'].endswith('.webp'):
            # 兼容旧生成器的截图命名；最终统一使用已审核的资源。
            img['src'] = prefix + 'assets/screenshots/batch-editor.webp'
        if '/screenshots/' in img.get('src',''):
            basename = Path(img['src']).name
            if basename not in {'batch-editor.webp','presets.webp','metadata-result.webp','privacy-result.webp'}:
                img['src'] = prefix + 'assets/screenshots/metadata-result.webp'
            width, height = Image.open(ROOT/'site/assets/screenshots'/Path(img['src']).name).size
            img['width'], img['height'] = str(width), str(height)
        img['decoding'] = 'async'
    for h3 in soup.select('.article-card h3'):
        a = h3.find('a')
        if a and primary:
            for key in GUIDES:
                route = {'metadata-editor':'iptc-exif-and-xmp-editing','privacy-cleanup':'private-metadata-cleanup','batch-presets':'batch-presets','photo-delivery':'photo-delivery-queue'}[key] if locale=='en-US' else key
                if route in a.get('href',''):
                    a.string = GUIDES[key][locale]['title']
                    card_image = h3.find_parent('article').find('img')
                    if card_image:
                        card_image['src'] = prefix + 'assets/screenshots/' + GUIDES[key]['image']
                        card_image['alt'] = GUIDES[key][locale]['title']
                        width, height = Image.open(ROOT/'site/assets/screenshots'/GUIDES[key]['image']).size
                        card_image['width'], card_image['height'] = str(width), str(height)
                    p = h3.parent.find('p', class_=None)
                    if p: p.string = GUIDES[key][locale]['intro']
    metadata(soup, locale, canonical, title, description, prefix, primary, version)
    stylesheet = soup.new_tag('link', rel='stylesheet', href=prefix+'assets/refinements.css')
    soup.head.append(stylesheet)
    path.write_text(str(soup), encoding='utf-8')
    return primary


def worker(paths):
    # 即使误把仓库根目录作为发布目录，非公开路径也不能透传到 ASSETS。
    allowed = set('/'+p for p in paths if p != '_worker.js')
    for p in list(allowed):
        if p.endswith('/index.html'):
            allowed.add(p[:-10])
            if p != '/index.html': allowed.add(p[:-11])
        elif p.endswith('.html'):
            allowed.add(p[:-5])
    return 'const allowed = new Set(' + json.dumps(sorted(allowed), ensure_ascii=False) + ''');
export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    let path;
    try { path = decodeURIComponent(url.pathname); } catch { return new Response("Bad request", {status: 400}); }
    if (!allowed.has(path)) return new Response("Not found", {status: 404, headers: {"cache-control": "no-store", "x-robots-tag": "noindex"}});
    if (path === "/google939576fea7c9232c.html") return new Response("google-site-verification: google939576fea7c9232c.html\\n", {headers: {"content-type": "text/html; charset=utf-8", "cache-control": "no-store"}});
    return env.ASSETS.fetch(request);
  }
};
'''


def build():
    public = ROOT / 'public'
    AUDIT.mkdir(exist_ok=True)
    record = AUDIT / 'generation-manifest.json'
    # Fresh Git checkouts contain the published assets and their ownership record.
    # Local audit state stays private; both records protect manual asset changes.
    versioned_record = ROOT / 'site/public-manifest.json'
    previous_record = record if record.exists() else versioned_record
    previous = json.loads(previous_record.read_text(encoding='utf-8')) if previous_record.exists() else None
    if public.exists():
        owned = {f['path']:f['sha256'] for f in previous['files']} if previous else {}
        conflicts = [p.relative_to(public).as_posix() for p in public.rglob('*') if p.is_file() and (p.relative_to(public).as_posix() not in owned or digest(p) != owned[p.relative_to(public).as_posix()])]
        if conflicts:
            raise RuntimeError('公开目录有人工作业，已保留，请先合并：' + ', '.join(conflicts[:10]))
    locales = {p.stem:yaml.safe_load(p.read_text(encoding='utf-8')) for p in (ROOT/'content/locales').glob('*.yaml')}
    app = yaml.safe_load((ROOT/'app-info.yaml').read_text(encoding='utf-8'))
    version = str(app['version']['name'])
    public_sources = json.loads((ROOT/'site/source-pages.json').read_text(encoding='utf-8'))
    with tempfile.TemporaryDirectory(prefix='captionmeta-site-') as temp:
        stage = Path(temp)
        for rel in public_sources:
            # 白名单类型加逐项文件路径，不复制配置、分析记录或模板。
            p = ROOT / rel
            safe = p.suffix in {'.html','.css','.js','.png','.jpg','.ico','.webmanifest','.xml','.txt','.mp4'} or p.name == '_headers'
            if not safe or p.name in {'llms.txt','robots.txt','sitemap.xml','_worker.js'} or rel.startswith('assets/'):
                continue
            if p.resolve().is_relative_to(ROOT) and p.is_file():
                dest = stage/rel; dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,dest)
        # 仅复制明确选择的资产，不发布旧封面和未经核验的视频。
        for name in ['styles.css','blog.css','locale-router.js','blog.js','google-play-badge.png','icon.png']:
            dest=stage/'assets'/name;dest.parent.mkdir(exist_ok=True);shutil.copy2(ROOT/'assets'/name,dest)
        for src in (ROOT/'site/assets').rglob('*'):
            if src.is_file():
                dest=stage/'assets'/src.relative_to(ROOT/'site/assets');dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,dest)
        icon=Image.open(ROOT/'assets/icon.png').convert('RGBA')
        icon.save(stage/'favicon.ico',sizes=[(16,16),(32,32),(48,48)])
        for name,size in [('favicon.png',96),('apple-touch-icon.png',180),('icon-192.png',192),('icon-512.png',512)]:
            icon.resize((size,size),Image.Resampling.LANCZOS).save(stage/'assets'/name)
        indexed=[]
        for path in stage.rglob('*.html'):
            rel=path.relative_to(stage).as_posix()
            if transform(path,rel,locales,version):
                soup=BeautifulSoup(path.read_text(encoding='utf-8'),'html.parser')
                indexed.append(soup.find('link',rel='canonical')['href'])
        for locale in sorted(PRIMARY):
            dest = stage / watch_path(locale).lstrip('/') / 'index.html'
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text(render_watch(locale), encoding='utf-8')
            indexed.append(SITE + watch_path(locale))
        manifest={'name':'CaptionMeta','short_name':'CaptionMeta','start_url':'/','display':'browser','background_color':'#ffffff','theme_color':'#1976d2','icons':[{'src':f'/assets/icon-{n}.png','sizes':f'{n}x{n}','type':'image/png'} for n in [192,512]]}
        (stage/'site.webmanifest').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
        ns='http://www.sitemaps.org/schemas/sitemap/0.9'; ET.register_namespace('',ns)
        sitemap=ET.Element('{'+ns+'}urlset')
        for url in sorted(indexed):
            entry=ET.SubElement(sitemap,'{'+ns+'}url');ET.SubElement(entry,'{'+ns+'}loc').text=url;ET.SubElement(entry,'{'+ns+'}lastmod').text=DAY
        ET.ElementTree(sitemap).write(stage/'sitemap.xml',encoding='utf-8',xml_declaration=True)
        # Video sitemap supplies discoverable metadata without inventing an unknown
        # first-publication date (required by Google's VideoObject rich results).
        video_ns = 'http://www.google.com/schemas/sitemap-video/1.1'
        ET.register_namespace('video', video_ns)
        video_map = ET.Element('{'+ns+'}urlset')
        for locale in sorted(PRIMARY):
            entry = ET.SubElement(video_map, '{'+ns+'}url')
            ET.SubElement(entry, '{'+ns+'}loc').text = SITE + watch_path(locale)
            video = ET.SubElement(entry, '{'+video_ns+'}video')
            for key, value in [('thumbnail_loc', SITE + THUMBNAIL), ('title', COPY[locale]['videoLabel']), ('description', COPY[locale]['videoCopy']), ('content_loc', SITE + VIDEO), ('duration', '29')]:
                ET.SubElement(video, '{'+video_ns+'}'+key).text = value
        ET.ElementTree(video_map).write(stage/'video-sitemap.xml', encoding='utf-8', xml_declaration=True)
        (stage/'robots.txt').write_text('User-agent: *\nAllow: /\n\nSitemap: '+SITE+'/sitemap.xml\nSitemap: '+SITE+'/video-sitemap.xml\n',encoding='utf-8')
        (stage/'llms.txt').write_text('# CaptionMeta\n\nAndroid photo metadata editor, listed on Google Play as Photo Metadata & IPTC Editor by AndroidManTou.\n\nEdit supported photo captions, keywords, credits and copyright. Reuse presets, inspect metadata cleanup, and deliver processed photos to a user-configured server. Format support varies. Metadata cleanup does not guarantee anonymity.\n\n## First-party pages\n- '+SITE+'/\n- '+SITE+'/en-US/\n- '+SITE+'/blog/en-US/\n- '+SITE+'/en-US/support\n\n## Download and privacy\n- '+PLAY+'\n- '+POLICY+'\n',encoding='utf-8')
        (stage/'_headers').write_text('/*\n  X-Content-Type-Options: nosniff\n  Referrer-Policy: strict-origin-when-cross-origin\n  X-Frame-Options: DENY\n  Permissions-Policy: camera=(), microphone=(), geolocation=()\n\n/assets/*\n  Cache-Control: public, max-age=3600\n',encoding='utf-8')
        files=sorted(p.relative_to(stage).as_posix() for p in stage.rglob('*') if p.is_file())
        code=worker(files)
        (stage/'_worker.js').write_text(code,encoding='utf-8')
        # Publish the same text bytes on Windows and Linux; ownership hashes must
        # survive Git checkout and rebuilding on either platform.
        for path in stage.rglob('*'):
            if path.is_file() and (path.suffix in {'.html','.css','.js','.xml','.txt','.webmanifest'} or path.name == '_headers'):
                path.write_bytes(path.read_bytes().replace(b'\r\n', b'\n'))
        # 在替换已归属文件前，先静态校验所有公开引用。
        sys.path.insert(0,str(ROOT/'site'))
        from validate_public import check
        check(stage)
        if public.exists():
            for old in previous['files']:
                target=public/old['path']
                if target.is_file() and not (stage/old['path']).exists(): target.unlink()
        shutil.copytree(stage,public,dirs_exist_ok=True)
        # 根目录 Worker 同样启用白名单，防止旧部署配置误公开内部文件。
        (ROOT/'_worker.js').write_text(code,encoding='utf-8')
    files=[{'path':p.relative_to(public).as_posix(),'sha256':digest(p),'owner':'generated','featureIds':[]} for p in sorted(public.rglob('*')) if p.is_file()]
    manifest_text = json.dumps({'schemaVersion':1,'generatedAt':DAY,'sourceRevision':None,'publicRoot':'public','files':files},ensure_ascii=False,indent=2)
    record.write_text(manifest_text,encoding='utf-8')
    versioned_record.write_text(manifest_text,encoding='utf-8')
    (AUDIT/'public-files.json').write_text(json.dumps([p['path'] for p in files],ensure_ascii=False,indent=2),encoding='utf-8')
    (ROOT/'static-site-manifest.json').write_text(json.dumps({'schemaVersion':'2.0','publicRoot':'public','entry':'index.html','files':[p['path'] for p in files]},ensure_ascii=False,indent=2),encoding='utf-8')
    print(f'OK: {len(files)} public files, {len(indexed)} indexable pages. Deploy only {public}')


if __name__ == '__main__':
    build()
