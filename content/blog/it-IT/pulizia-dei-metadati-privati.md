---
contentId: privacy-cleanup
locale: it-IT
status: machine-draft
title: 'Pulizia dei metadati privati: what it does in CaptionMeta'
description: Controlla e pulisci dati EXIF, IPTC e XMP selezionati prima di condividere
  una copia elaborata. Learn the exact problem, options, verified steps, and known
  limitations.
slug: pulizia-dei-metadati-privati
intent: feature education
audience: app users
canonical: ''
evidence:
- core/core_exif/src/main/java/com/wkq/util/exif/MetadataScrubber.kt
- core/core_exif/src/test/java/com/wkq/util/exif/MetadataScrubberTest.kt
- doc/privacy_policy.html
primaryKeyword: 'Pulizia dei metadati privati: what it does in CaptionMeta'
relatedPages:
- /
- /support
template: standard-article
---

# Pulizia dei metadati privati: what it does in CaptionMeta

Una foto può contenere posizione, fotocamera e altri metadati che non devono essere inclusi in ogni consegna.

## What this feature helps you do

- Controllare le categorie di metadati EXIF, IPTC e XMP tracciate
- Rimuovere metadati privati selezionati da una copia elaborata
- Tenere separati il file originale e il flusso di output pulito

## Where it fits in the workflow

- Seleziona la foto da controllare
- Esamina le categorie di metadati disponibili per la pulizia
- Esegui la pulizia e usa la copia per la consegna

## What to check before export

- Categorie di posizione, fotocamera e altri metadati tracciati dal flusso di pulizia

## What to keep in mind

- La pulizia si basa sulle categorie implementate nella versione attuale; controlla l’output prima della pubblicazione.

