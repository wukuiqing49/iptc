---
contentId: photo-delivery
locale: zh-CN
status: draft
title: 照片交付队列：在 CaptionMeta 中能做什么
description: 将处理后的照片加入队列，通过已配置的服务器完成交付并查看结果。 了解它解决的问题、具体选项、真实操作步骤和已知限制。
slug: photo-delivery
intent: feature education
audience: app users
canonical: ''
evidence:
- core/core_upload/src/main/java/com/wkq/iptc/upload/UploadDispatcher.kt
- core/core_upload/src/main/java/com/wkq/iptc/upload/http/RetryInterceptor.kt
- core/core_upload/consumer-rules.pro
primaryKeyword: 照片交付队列：在 CaptionMeta 中能做什么
relatedPages:
- /
- /support.html
template: standard-article
---

# 照片交付队列：在 CaptionMeta 中能做什么

现场照片交付容易受到文件、服务器设置和失败重试状态分散管理的影响。

## 这项功能解决什么问题

- 将处理后的照片加入交付队列。
- 支持已配置的 FTP、FTPS、SFTP、HTTP、SMB 和 WebDAV 客户端。
- 对部分临时 HTTP 失败进行重试，并保留上传任务结果供检查。

## 如何融入处理流程

- 配置交付服务器。
- 选择处理后的照片并加入上传队列。
- 查看队列、重试符合条件的失败任务，并检查历史记录。

## 导出前需要检查什么

- FTP、FTPS、SFTP、HTTP、SMB 和 WebDAV 服务器配置。

## 注意事项

- 交付需要用户配置的可访问服务器和凭据；应用不提供托管照片存储服务。

