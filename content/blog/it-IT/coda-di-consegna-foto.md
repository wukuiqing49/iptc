---
contentId: photo-delivery
locale: it-IT
status: machine-draft
title: 'Coda di consegna foto: what it does in CaptionMeta'
description: Metti in coda le foto elaborate, consegnale tramite server configurati
  e controlla i risultati. Learn the exact problem, options, verified steps, and known
  limitations.
slug: coda-di-consegna-foto
intent: feature education
audience: app users
canonical: ''
evidence:
- core/core_upload/src/main/java/com/wkq/iptc/upload/UploadDispatcher.kt
- core/core_upload/src/main/java/com/wkq/iptc/upload/http/RetryInterceptor.kt
- core/core_upload/consumer-rules.pro
primaryKeyword: 'Coda di consegna foto: what it does in CaptionMeta'
relatedPages:
- /
- /support
template: standard-article
---

# Coda di consegna foto: what it does in CaptionMeta

La consegna delle foto sul campo può fallire quando file, server e stato dei tentativi sono gestiti separatamente.

## What this feature helps you do

- Mettere in coda i file fotografici elaborati
- Supportare client configurati FTP, FTPS, SFTP, HTTP, SMB e WebDAV
- Riprovare alcuni errori HTTP temporanei e conservare i risultati delle attività

## Where it fits in the workflow

- Configura un profilo del server di consegna
- Scegli le foto elaborate e aggiungile alla coda
- Controlla la coda, riprova gli errori idonei e consulta la cronologia

## What to check before export

- Profili server FTP, FTPS, SFTP, HTTP, SMB e WebDAV

## What to keep in mind

- La consegna richiede un server raggiungibile e credenziali configurate dall’utente. L’app non offre spazio fotografico ospitato.

