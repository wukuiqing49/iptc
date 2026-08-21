---
contentId: batch-presets
locale: es-419
status: machine-draft
title: 'Ajustes preestablecidos por lote: what it does in CaptionMeta'
description: Reutiliza ajustes IPTC en un grupo de fotos y conserva las modificaciones
  individuales. Learn the exact problem, options, verified steps, and known limitations.
slug: ajustes-preestablecidos-por-lote
intent: feature education
audience: app users
canonical: ''
evidence:
- core/core_exif/src/test/java/com/wkq/iptc/feature/press/model/MetadataTemplateWorkflowTest.kt
- feature/feature_app/src/test/java/com/wkq/iptc/feature/press/workflow/WorkflowResolverTest.kt
- feature/feature_app/src/main/res/values/strings.xml
primaryKeyword: 'Ajustes preestablecidos por lote: what it does in CaptionMeta'
relatedPages:
- /
- /support
template: standard-article
---

# Ajustes preestablecidos por lote: what it does in CaptionMeta

Los trabajos repetidos necesitan metadatos consistentes sin volver a escribir los mismos campos para cada foto.

## What this feature helps you do

- Crear y reutilizar plantillas o ajustes de metadatos
- Aplicar valores por lote a varias fotos seleccionadas
- Usar modificaciones por foto cuando una imagen necesita otro pie de foto o campo

## Where it fits in the workflow

- Elige o crea un ajuste IPTC
- Selecciona los campos y fotos que quieres procesar
- Revisa las modificaciones por foto y escribe los valores finales

## What to check before export

- Campos del ajuste, valores del lote, modificaciones por foto, autor, ubicación y configuración de entrega

## What to keep in mind

- Un ajuste solo afecta a los campos configurados para ese flujo; los campos vacíos o desactivados no se consideran rellenados.

