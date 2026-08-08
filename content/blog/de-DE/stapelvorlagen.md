---
contentId: batch-presets
locale: de-DE
status: machine-draft
title: 'Stapelvorlagen: what it does in CaptionMeta'
description: IPTC-Vorlagen für mehrere Fotos wiederverwenden und individuelle Überschreibungen
  beibehalten. Learn the exact problem, options, verified steps, and known limitations.
slug: stapelvorlagen
intent: feature education
audience: app users
canonical: ''
evidence:
- core/core_exif/src/test/java/com/wkq/iptc/feature/press/model/MetadataTemplateWorkflowTest.kt
- feature/feature_app/src/test/java/com/wkq/iptc/feature/press/workflow/WorkflowResolverTest.kt
- feature/feature_app/src/main/res/values/strings.xml
primaryKeyword: 'Stapelvorlagen: what it does in CaptionMeta'
relatedPages:
- /
- /support.html
template: standard-article
---

# Stapelvorlagen: what it does in CaptionMeta

Bei wiederholten Fotoaufträgen ist es schwer, konsistent zu bleiben, wenn dieselben Felder für jedes Bild neu eingegeben werden.

## What this feature helps you do

- Metadatentemplates oder Vorlagen erstellen und wiederverwenden
- Stapelwerte auf mehrere ausgewählte Fotos anwenden
- Einzelne Fotos mit abweichender Bildunterschrift oder Feldwert überschreiben

## Where it fits in the workflow

- Eine IPTC-Vorlage wählen oder erstellen
- Stapelwerte und zu verarbeitende Fotos auswählen
- Einzelbildüberschreibungen prüfen und die endgültigen Werte schreiben

## What to check before export

- Vorlagenfelder, Stapelwerte, Einzelbildüberschreibungen, Urheber, Standort und Übergabeeinstellungen

## What to keep in mind

- Eine Vorlage wirkt nur auf die konfigurierten Felder. Leere oder deaktivierte Felder werden nicht als befüllt angenommen.

