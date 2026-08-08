---
contentId: privacy-cleanup
locale: es-419
status: machine-draft
title: 'Limpieza de metadatos privados: what it does in CaptionMeta'
description: Inspecciona y limpia datos EXIF, IPTC y XMP seleccionados antes de compartir
  una copia procesada. Learn the exact problem, options, verified steps, and known
  limitations.
slug: limpieza-de-metadatos-privados
intent: feature education
audience: app users
canonical: ''
evidence:
- core/core_exif/src/main/java/com/wkq/util/exif/MetadataScrubber.kt
- core/core_exif/src/test/java/com/wkq/util/exif/MetadataScrubberTest.kt
- doc/privacy_policy.html
primaryKeyword: 'Limpieza de metadatos privados: what it does in CaptionMeta'
relatedPages:
- /
- /support.html
template: standard-article
---

# Limpieza de metadatos privados: what it does in CaptionMeta

Una foto puede incluir ubicación, cámara y otros metadatos que no deberían estar en cada entrega.

## What this feature helps you do

- Inspeccionar categorías de metadatos EXIF, IPTC y XMP registradas
- Eliminar metadatos privados seleccionados de una copia procesada
- Mantener separado el archivo original del flujo de salida limpio

## Where it fits in the workflow

- Selecciona la foto que quieres inspeccionar
- Revisa las categorías disponibles para limpiar
- Ejecuta la limpieza y usa la copia procesada para la entrega

## What to check before export

- Categorías de ubicación, cámara y otros metadatos registrados por el flujo de limpieza

## What to keep in mind

- La limpieza se basa en las categorías implementadas por la versión actual; revisa el resultado antes de publicarlo.

