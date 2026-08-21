---
contentId: metadata-editor
locale: es-419
status: machine-draft
title: 'Edición IPTC, EXIF y XMP: what it does in CaptionMeta'
description: Revisa y edita pies de foto, titulares, palabras clave, autores, copyright,
  derechos y ubicación. Learn the exact problem, options, verified steps, and known
  limitations.
slug: edición-iptc-exif-y-xmp
intent: feature education
audience: app users
canonical: ''
evidence:
- core/core_exif/src/main/java/com/wkq/util/exif/MetadataScrubber.kt
- core/core_exif/src/test/java/com/wkq/iptc/feature/press/metadata/IptcAndXmpVerificationTest.kt
- feature/feature_app/src/main/res/values/strings.xml
primaryKeyword: 'Edición IPTC, EXIF y XMP: what it does in CaptionMeta'
relatedPages:
- /
- /support
template: standard-article
---

# Edición IPTC, EXIF y XMP: what it does in CaptionMeta

Las entregas se vuelven inconsistentes cuando los pies de foto, créditos, derechos o palabras clave se editan de manera distinta para cada imagen.

## What this feature helps you do

- Leer e inspeccionar metadatos EXIF, IPTC y XMP compatibles
- Escribir pies de foto, titulares, palabras clave, autores, copyright, derechos y ubicación en copias procesadas
- Usar valores por foto para ajustar o reemplazar valores del lote

## Where it fits in the workflow

- Selecciona una foto o un grupo de fotos locales
- Elige un ajuste o introduce pies de foto, titulares, palabras clave, autor y derechos
- Revisa el resultado y guarda la copia procesada

## What to check before export

- Campos IPTC principales y extendidos, campos XMP, gestión EXIF y valores de ubicación

## What to keep in mind

- Los campos disponibles y el comportamiento de escritura dependen del archivo seleccionado y de los campos activados en el flujo.

