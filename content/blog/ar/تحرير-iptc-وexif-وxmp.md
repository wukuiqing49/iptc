---
contentId: metadata-editor
locale: ar
status: machine-draft
title: 'تحرير IPTC وEXIF وXMP: what it does in CaptionMeta'
description: راجع وحرّر العناوين والترويسات والكلمات المفتاحية والمؤلفين وحقوق النشر
  والحقوق والموقع. Learn the exact problem, options, verified steps, and known limitations.
slug: تحرير-iptc-وexif-وxmp
intent: feature education
audience: app users
canonical: ''
evidence:
- core/core_exif/src/main/java/com/wkq/util/exif/MetadataScrubber.kt
- core/core_exif/src/test/java/com/wkq/iptc/feature/press/metadata/IptcAndXmpVerificationTest.kt
- feature/feature_app/src/main/res/values/strings.xml
primaryKeyword: 'تحرير IPTC وEXIF وXMP: what it does in CaptionMeta'
relatedPages:
- /
- /support.html
template: standard-article
---

# تحرير IPTC وEXIF وXMP: what it does in CaptionMeta

تصبح عمليات تسليم الصور غير متسقة عندما تُحرّر العناوين والاعتمادات والحقوق والكلمات المفتاحية بشكل مختلف لكل صورة.

## What this feature helps you do

- قراءة وفحص بيانات EXIF وIPTC وXMP المدعومة
- كتابة العناوين والترويسات والكلمات المفتاحية والمؤلفين وحقوق النشر والحقوق والموقع في نسخ الصور المعالجة
- استخدام قيم لكل صورة لتحسين قيم الدفعة أو استبدالها

## Where it fits in the workflow

- اختر صورة واحدة أو مجموعة صور محلية
- اختر إعداداً مسبقاً أو أدخل العناوين والترويسات والكلمات المفتاحية والمؤلف والحقوق
- راجع النتيجة واحفظ النسخة المعالجة

## What to check before export

- حقول IPTC الأساسية والموسعة وحقول XMP ومعالجة EXIF وقيم الموقع

## What to keep in mind

- تعتمد الحقول المتاحة وسلوك الكتابة على الملف المختار والحقول المفعّلة في سير العمل.

