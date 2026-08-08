---
contentId: metadata-editor
locale: ru-RU
status: machine-draft
title: 'Редактирование IPTC, EXIF и XMP: what it does in CaptionMeta'
description: Просматривайте и редактируйте подписи, заголовки, ключевые слова, авторов,
  авторские права и местоположение. Learn the exact problem, options, verified steps,
  and known limitations.
slug: редактирование-iptc-exif-и-xmp
intent: feature education
audience: app users
canonical: ''
evidence:
- core/core_exif/src/main/java/com/wkq/util/exif/MetadataScrubber.kt
- core/core_exif/src/test/java/com/wkq/iptc/feature/press/metadata/IptcAndXmpVerificationTest.kt
- feature/feature_app/src/main/res/values/strings.xml
primaryKeyword: 'Редактирование IPTC, EXIF и XMP: what it does in CaptionMeta'
relatedPages:
- /
- /support.html
template: standard-article
---

# Редактирование IPTC, EXIF и XMP: what it does in CaptionMeta

Передача фотографий становится непоследовательной, если подписи, авторство, права и ключевые слова редактируются по-разному для каждого изображения.

## What this feature helps you do

- Читать и проверять поддерживаемые метаданные EXIF, IPTC и XMP
- Записывать подписи, заголовки, ключевые слова, авторство, права и местоположение в обработанные копии
- Уточнять или заменять пакетные значения значениями для отдельной фотографии

## Where it fits in the workflow

- Выберите одну фотографию или группу локальных фотографий
- Выберите шаблон или введите подписи, заголовки, ключевые слова, автора и права
- Проверьте результат и сохраните обработанную копию

## What to check before export

- Основные и расширенные поля IPTC, поля XMP, обработка EXIF и местоположение

## What to keep in mind

- Доступные поля и поведение записи зависят от выбранного файла и включённых в процессе полей.

