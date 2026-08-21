---
contentId: photo-delivery
locale: en-US
status: machine-draft
title: 'Photo delivery queue: what it does in CaptionMeta'
description: Queue processed photos, deliver them through configured servers, and
  review task results. Learn the exact problem, options, verified steps, and known
  limitations.
slug: photo-delivery-queue
intent: feature education
audience: app users
canonical: ''
evidence:
- core/core_upload/src/main/java/com/wkq/iptc/upload/UploadDispatcher.kt
- core/core_upload/src/main/java/com/wkq/iptc/upload/http/RetryInterceptor.kt
- core/core_upload/consumer-rules.pro
primaryKeyword: 'Photo delivery queue: what it does in CaptionMeta'
relatedPages:
- /
- /support
template: standard-article
---

# Photo delivery queue: what it does in CaptionMeta

Field photo delivery can fail when files, server settings, and retry state are managed in separate places.

## What this feature helps you do

- Queue processed photo files for delivery.
- Support configured FTP, FTPS, SFTP, HTTP, SMB, and WebDAV clients.
- Retry selected transient HTTP failures and keep upload task results for review.

## Where it fits in the workflow

- Configure a delivery server profile.
- Choose processed photos and add them to the upload queue.
- Monitor the queue, retry eligible failures, and review history.

## What to check before export

- FTP, FTPS, SFTP, HTTP, SMB, and WebDAV server profiles.

## What to keep in mind

- Delivery requires a reachable server and credentials configured by the user; the app does not provide hosted photo storage.

