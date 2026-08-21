---
contentId: metadata-editor
locale: zh-CN
status: draft
title: IPTC、EXIF 与 XMP 编辑：在 CaptionMeta 中能做什么
description: 查看并编辑说明、标题、关键词、署名、版权、权利和位置等照片元数据。 了解它解决的问题、具体选项、真实操作步骤和已知限制。
slug: metadata-editor
intent: feature education
audience: app users
canonical: ''
evidence:
- core/core_exif/src/main/java/com/wkq/util/exif/MetadataScrubber.kt
- core/core_exif/src/test/java/com/wkq/iptc/feature/press/metadata/IptcAndXmpVerificationTest.kt
- feature/feature_app/src/main/res/values/strings.xml
primaryKeyword: IPTC、EXIF 与 XMP 编辑：在 CaptionMeta 中能做什么
relatedPages:
- /
- /support
template: standard-article
---

# IPTC、EXIF 与 XMP 编辑：在 CaptionMeta 中能做什么

当每张照片的说明、署名、权利或关键词都被单独编辑时，交付内容容易不一致。

## 这项功能解决什么问题

- 读取并检查支持的 EXIF、IPTC 和 XMP 元数据。
- 将说明、标题、关键词、署名、版权、权利和位置写入处理后的照片副本。
- 使用单张照片的值细化或覆盖批量值。

## 如何融入处理流程

- 选择一张或一组本地照片。
- 选择预设，或填写说明、标题、关键词、署名和权利字段。
- 检查结果并保存处理后的副本，用于分享或交付。

## 导出前需要检查什么

- IPTC 核心与扩展字段、XMP 字段、EXIF 处理和位置值。

## 注意事项

- 可用字段和写入行为取决于所选文件以及工作流中启用的元数据字段。

