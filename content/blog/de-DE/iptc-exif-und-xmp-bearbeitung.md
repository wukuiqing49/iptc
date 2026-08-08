---
contentId: metadata-editor
locale: de-DE
status: machine-draft
title: 'IPTC-, EXIF- und XMP-Bearbeitung: what it does in CaptionMeta'
description: Bildunterschriften, Überschriften, Keywords, Urheber, Copyright, Rechte
  und Standortdaten prüfen und bearbeiten. Learn the exact problem, options, verified
  steps, and known limitations.
slug: iptc-exif-und-xmp-bearbeitung
intent: feature education
audience: app users
canonical: ''
evidence:
- core/core_exif/src/main/java/com/wkq/util/exif/MetadataScrubber.kt
- core/core_exif/src/test/java/com/wkq/iptc/feature/press/metadata/IptcAndXmpVerificationTest.kt
- feature/feature_app/src/main/res/values/strings.xml
primaryKeyword: 'IPTC-, EXIF- und XMP-Bearbeitung: what it does in CaptionMeta'
relatedPages:
- /
- /support.html
template: standard-article
---

# IPTC-, EXIF- und XMP-Bearbeitung: what it does in CaptionMeta

Wenn Bildunterschriften, Credits, Rechte oder Keywords für jedes Bild anders bearbeitet werden, werden Fotoübergaben uneinheitlich.

## What this feature helps you do

- Unterstützte EXIF-, IPTC- und XMP-Metadaten lesen und prüfen
- Bildunterschriften, Überschriften, Keywords, Urheber, Copyright, Rechte und Standortfelder in bearbeitete Fotokopien schreiben
- Einzelbildwerte zur Verfeinerung oder Überschreibung von Stapelwerten nutzen

## Where it fits in the workflow

- Ein einzelnes Foto oder eine Gruppe lokaler Fotos auswählen
- Eine Vorlage wählen oder Bildunterschriften, Überschriften, Keywords, Urheber und Rechte eingeben
- Das Ergebnis prüfen und die bearbeitete Kopie speichern

## What to check before export

- IPTC-Kern- und Erweiterungsfelder, XMP-Felder, EXIF-Verarbeitung und Standortwerte

## What to keep in mind

- Verfügbare Felder und Schreibverhalten hängen von der ausgewählten Datei und den im Workflow aktivierten Metadatenfeldern ab.

