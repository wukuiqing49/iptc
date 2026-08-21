---
contentId: privacy-cleanup
locale: zh-CN
status: draft
title: 隐私元数据清理：在 CaptionMeta 中能做什么
description: 在分享处理后的照片副本前，检查并清理选定的 EXIF、IPTC 和 XMP 信息。 了解它解决的问题、具体选项、真实操作步骤和已知限制。
slug: privacy-cleanup
intent: feature education
audience: app users
canonical: ''
evidence:
- core/core_exif/src/main/java/com/wkq/util/exif/MetadataScrubber.kt
- core/core_exif/src/test/java/com/wkq/util/exif/MetadataScrubberTest.kt
- doc/privacy_policy.html
primaryKeyword: 隐私元数据清理：在 CaptionMeta 中能做什么
relatedPages:
- /
- /support
template: standard-article
---

# 隐私元数据清理：在 CaptionMeta 中能做什么

照片可能携带位置、相机和其他元数据，而这些信息并不适合出现在每一次交付中。

## 这项功能解决什么问题

- 检查已跟踪的 EXIF、IPTC 和 XMP 元数据类别。
- 从处理后的照片副本中清理选定的隐私元数据。
- 将原始文件与清理后的输出流程分开处理。

## 如何融入处理流程

- 选择要检查的照片。
- 查看可清理的元数据类别。
- 执行清理，并将处理后的副本用于交付。

## 导出前需要检查什么

- 工作流中提供的位置、相机和其他已跟踪元数据类别。

## 注意事项

- 清理范围基于当前版本实现的元数据类别；发布前请检查输出结果。

