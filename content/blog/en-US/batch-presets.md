---
contentId: batch-presets
locale: en-US
status: machine-draft
title: 'Batch presets: what it does in CaptionMeta'
description: Reuse IPTC presets across a group of photos while retaining per-photo
  overrides. Learn the exact problem, options, verified steps, and known limitations.
slug: batch-presets
intent: feature education
audience: app users
canonical: ''
evidence:
- core/core_exif/src/test/java/com/wkq/iptc/feature/press/model/MetadataTemplateWorkflowTest.kt
- feature/feature_app/src/test/java/com/wkq/iptc/feature/press/workflow/WorkflowResolverTest.kt
- feature/feature_app/src/main/res/values/strings.xml
primaryKeyword: 'Batch presets: what it does in CaptionMeta'
relatedPages:
- /
- /support.html
template: standard-article
---

# Batch presets: what it does in CaptionMeta

Repeated photo assignments need consistent metadata without retyping the same fields for every image.

## What this feature helps you do

- Create and reuse metadata templates or presets.
- Apply batch values to multiple selected photos.
- Use per-photo overrides when one image needs a different caption or field value.

## Where it fits in the workflow

- Choose or create an IPTC preset.
- Select batch fields and photos to process.
- Review per-photo overrides and write resolved values to processed copies.

## What to check before export

- Preset fields, batch values, per-photo overrides, byline, location, and delivery settings.

## What to keep in mind

- A preset only affects fields configured for that workflow; empty or disabled fields are not implied to contain data.

