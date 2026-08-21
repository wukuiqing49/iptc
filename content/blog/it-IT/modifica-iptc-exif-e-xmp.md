---
contentId: metadata-editor
locale: it-IT
status: machine-draft
title: 'Modifica IPTC, EXIF e XMP: what it does in CaptionMeta'
description: Controlla e modifica didascalie, titoli, parole chiave, autori, copyright,
  diritti e posizione. Learn the exact problem, options, verified steps, and known
  limitations.
slug: modifica-iptc-exif-e-xmp
intent: feature education
audience: app users
canonical: ''
evidence:
- core/core_exif/src/main/java/com/wkq/util/exif/MetadataScrubber.kt
- core/core_exif/src/test/java/com/wkq/iptc/feature/press/metadata/IptcAndXmpVerificationTest.kt
- feature/feature_app/src/main/res/values/strings.xml
primaryKeyword: 'Modifica IPTC, EXIF e XMP: what it does in CaptionMeta'
relatedPages:
- /
- /support
template: standard-article
---

# Modifica IPTC, EXIF e XMP: what it does in CaptionMeta

Le consegne diventano incoerenti quando didascalie, crediti, diritti o parole chiave vengono modificati in modo diverso per ogni immagine.

## What this feature helps you do

- Leggere e controllare i metadati EXIF, IPTC e XMP supportati
- Scrivere didascalie, titoli, parole chiave, autori, copyright, diritti e posizione nelle copie elaborate
- Usare valori per foto per perfezionare o sostituire i valori del batch

## Where it fits in the workflow

- Seleziona una foto o un gruppo di foto locali
- Scegli un preset oppure inserisci didascalie, titoli, parole chiave, autore e diritti
- Controlla il risultato e salva la copia elaborata

## What to check before export

- Campi IPTC principali ed estesi, campi XMP, gestione EXIF e valori di posizione

## What to keep in mind

- I campi disponibili e il comportamento di scrittura dipendono dal file selezionato e dai campi attivati nel flusso.

