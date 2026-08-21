---
contentId: batch-presets
locale: it-IT
status: machine-draft
title: 'Preset in batch: what it does in CaptionMeta'
description: Riutilizza preset IPTC su più foto mantenendo le modifiche per singola
  foto. Learn the exact problem, options, verified steps, and known limitations.
slug: preset-in-batch
intent: feature education
audience: app users
canonical: ''
evidence:
- core/core_exif/src/test/java/com/wkq/iptc/feature/press/model/MetadataTemplateWorkflowTest.kt
- feature/feature_app/src/test/java/com/wkq/iptc/feature/press/workflow/WorkflowResolverTest.kt
- feature/feature_app/src/main/res/values/strings.xml
primaryKeyword: 'Preset in batch: what it does in CaptionMeta'
relatedPages:
- /
- /support
template: standard-article
---

# Preset in batch: what it does in CaptionMeta

I lavori ripetuti richiedono metadati coerenti senza riscrivere gli stessi campi per ogni foto.

## What this feature helps you do

- Creare e riutilizzare modelli o preset di metadati
- Applicare valori batch a più foto selezionate
- Usare modifiche per singola foto quando un’immagine richiede una didascalia o un campo diverso

## Where it fits in the workflow

- Scegli o crea un preset IPTC
- Seleziona campi e foto da elaborare
- Controlla le modifiche per foto e scrivi i valori finali

## What to check before export

- Campi del preset, valori batch, modifiche per foto, autore, posizione e impostazioni di consegna

## What to keep in mind

- Un preset agisce solo sui campi configurati per quel flusso; i campi vuoti o disattivati non vengono considerati valorizzati.

