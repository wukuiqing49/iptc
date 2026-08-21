---
contentId: metadata-editor
locale: en-US
status: machine-draft
title: 'IPTC, EXIF, and XMP editing: what it does in CaptionMeta'
description: Review and edit captions, headlines, keywords, bylines, copyright, rights,
  and location metadata. Learn the exact problem, options, verified steps, and known
  limitations.
slug: iptc-exif-and-xmp-editing
intent: feature education
audience: app users
canonical: ''
evidence:
- core/core_exif/src/main/java/com/wkq/util/exif/MetadataScrubber.kt
- core/core_exif/src/test/java/com/wkq/iptc/feature/press/metadata/IptcAndXmpVerificationTest.kt
- feature/feature_app/src/main/res/values/strings.xml
primaryKeyword: 'IPTC, EXIF, and XMP editing: what it does in CaptionMeta'
relatedPages:
- /
- /support
template: standard-article
---

# IPTC, EXIF, and XMP editing: what it does in CaptionMeta

Photo handoffs become inconsistent when captions, credits, rights, or keywords are edited differently for every image.

## What this feature helps you do

- Read and inspect supported EXIF, IPTC, and XMP metadata.
- Write captions, headlines, keywords, bylines, copyright, rights, and location fields into processed photo copies.
- Use per-photo values to refine or override batch values.

## Where it fits in the workflow

- Select a local photo or group of photos.
- Choose a preset or enter captions, headlines, keywords, bylines, and rights.
- Review the result and save the processed copy for sharing or delivery.

## What to check before export

- IPTC core and extended fields, XMP fields, EXIF handling, and location values.

## What to keep in mind

- Available fields and write behavior depend on the selected file and the metadata fields enabled in the workflow.

