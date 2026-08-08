---
contentId: privacy-cleanup
locale: en-US
status: machine-draft
title: 'Private metadata cleanup: what it does in CaptionMeta'
description: Inspect and clean selected EXIF, IPTC, and XMP data before sharing a
  processed photo copy. Learn the exact problem, options, verified steps, and known
  limitations.
slug: private-metadata-cleanup
intent: feature education
audience: app users
canonical: ''
evidence:
- core/core_exif/src/main/java/com/wkq/util/exif/MetadataScrubber.kt
- core/core_exif/src/test/java/com/wkq/util/exif/MetadataScrubberTest.kt
- doc/privacy_policy.html
primaryKeyword: 'Private metadata cleanup: what it does in CaptionMeta'
relatedPages:
- /
- /support.html
template: standard-article
---

# Private metadata cleanup: what it does in CaptionMeta

A photo can carry location, camera, and other metadata that should not be included in every delivery.

## What this feature helps you do

- Inspect tracked EXIF, IPTC, and XMP metadata categories.
- Scrub selected private metadata from a processed photo copy.
- Keep the original file separate from the cleaned output workflow.

## Where it fits in the workflow

- Select the photo to inspect.
- Review the metadata categories available for cleanup.
- Run cleanup and use the processed copy for the intended delivery.

## What to check before export

- Location, camera, and other tracked metadata categories exposed by the cleanup workflow.

## What to keep in mind

- Cleanup is based on metadata categories implemented by the current app version; review the output before publication.

