---
contentId: privacy-cleanup
locale: de-DE
status: machine-draft
title: 'Private Metadaten bereinigen: what it does in CaptionMeta'
description: Ausgewählte EXIF-, IPTC- und XMP-Daten vor dem Teilen einer bearbeiteten
  Fotokopie prüfen und entfernen. Learn the exact problem, options, verified steps,
  and known limitations.
slug: private-metadaten-bereinigen
intent: feature education
audience: app users
canonical: ''
evidence:
- core/core_exif/src/main/java/com/wkq/util/exif/MetadataScrubber.kt
- core/core_exif/src/test/java/com/wkq/util/exif/MetadataScrubberTest.kt
- doc/privacy_policy.html
primaryKeyword: 'Private Metadaten bereinigen: what it does in CaptionMeta'
relatedPages:
- /
- /support.html
template: standard-article
---

# Private Metadaten bereinigen: what it does in CaptionMeta

Ein Foto kann Standort-, Kamera- und weitere Metadaten enthalten, die nicht in jede Übergabe gehören.

## What this feature helps you do

- Erfasste EXIF-, IPTC- und XMP-Metadatenkategorien prüfen
- Ausgewählte private Metadaten aus einer bearbeiteten Fotokopie entfernen
- Originaldatei und bereinigten Ausgabe-Workflow getrennt behandeln

## Where it fits in the workflow

- Das zu prüfende Foto auswählen
- Die für die Bereinigung verfügbaren Kategorien prüfen
- Die Bereinigung ausführen und die Kopie für die Übergabe verwenden

## What to check before export

- Standort-, Kamera- und weitere im Bereinigungs-Workflow erfasste Metadatenkategorien

## What to keep in mind

- Der Umfang richtet sich nach den in der aktuellen App-Version implementierten Kategorien. Ausgabe vor der Veröffentlichung prüfen.

