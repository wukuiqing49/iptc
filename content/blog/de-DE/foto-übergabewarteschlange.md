---
contentId: photo-delivery
locale: de-DE
status: machine-draft
title: 'Foto-Übergabewarteschlange: what it does in CaptionMeta'
description: Bearbeitete Fotos einreihen, über konfigurierte Server übertragen und
  Aufgabenergebnisse prüfen. Learn the exact problem, options, verified steps, and
  known limitations.
slug: foto-übergabewarteschlange
intent: feature education
audience: app users
canonical: ''
evidence:
- core/core_upload/src/main/java/com/wkq/iptc/upload/UploadDispatcher.kt
- core/core_upload/src/main/java/com/wkq/iptc/upload/http/RetryInterceptor.kt
- core/core_upload/consumer-rules.pro
primaryKeyword: 'Foto-Übergabewarteschlange: what it does in CaptionMeta'
relatedPages:
- /
- /support.html
template: standard-article
---

# Foto-Übergabewarteschlange: what it does in CaptionMeta

Die Übergabe von Fotos aus dem Einsatz kann scheitern, wenn Dateien, Servereinstellungen und Wiederholungsstatus getrennt verwaltet werden.

## What this feature helps you do

- Bearbeitete Fotodateien zur Übergabe einreihen
- Konfigurierte FTP-, FTPS-, SFTP-, HTTP-, SMB- und WebDAV-Clients unterstützen
- Bestimmte vorübergehende HTTP-Fehler wiederholen und Aufgabenergebnisse behalten

## Where it fits in the workflow

- Ein Übergabeserverprofil konfigurieren
- Bearbeitete Fotos auswählen und zur Upload-Warteschlange hinzufügen
- Warteschlange überwachen, geeignete Fehler wiederholen und Verlauf prüfen

## What to check before export

- Serverprofile für FTP, FTPS, SFTP, HTTP, SMB und WebDAV

## What to keep in mind

- Die Übergabe benötigt einen erreichbaren Server und vom Benutzer konfigurierte Zugangsdaten. Die App bietet keinen gehosteten Fotospeicher.

