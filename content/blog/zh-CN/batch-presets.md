---
contentId: batch-presets
locale: zh-CN
status: draft
title: 批量预设：在 CaptionMeta 中能做什么
description: 复用 IPTC 预设，将共同字段应用到一组照片，并保留单张照片覆盖能力。 了解它解决的问题、具体选项、真实操作步骤和已知限制。
slug: batch-presets
intent: feature education
audience: app users
canonical: ''
evidence:
- core/core_exif/src/test/java/com/wkq/iptc/feature/press/model/MetadataTemplateWorkflowTest.kt
- feature/feature_app/src/test/java/com/wkq/iptc/feature/press/workflow/WorkflowResolverTest.kt
- feature/feature_app/src/main/res/values/strings.xml
primaryKeyword: 批量预设：在 CaptionMeta 中能做什么
relatedPages:
- /
- /support
template: standard-article
---

# 批量预设：在 CaptionMeta 中能做什么

重复处理一批照片时，如果每次都重新输入相同字段，就很难保持一致。

## 这项功能解决什么问题

- 创建并复用元数据模板或预设。
- 将批量值应用到多张选中的照片。
- 在单张照片需要不同说明或字段值时使用单张覆盖。

## 如何融入处理流程

- 选择或创建 IPTC 预设。
- 选择批量字段和要处理的照片。
- 检查单张覆盖值，并将最终值写入处理后的副本。

## 导出前需要检查什么

- 预设字段、批量值、单张覆盖、署名、位置和交付设置。

## 注意事项

- 预设只影响该工作流配置的字段；空字段或停用字段不会被推断为有值。

