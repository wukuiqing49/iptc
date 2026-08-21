---
contentId: privacy-cleanup
locale: pt-PT
status: machine-draft
title: 'Limpeza de metadados privados: what it does in CaptionMeta'
description: Inspecione e limpe dados EXIF, IPTC e XMP selecionados antes de partilhar
  uma cópia processada. Learn the exact problem, options, verified steps, and known
  limitations.
slug: limpeza-de-metadados-privados
intent: feature education
audience: app users
canonical: ''
evidence:
- core/core_exif/src/main/java/com/wkq/util/exif/MetadataScrubber.kt
- core/core_exif/src/test/java/com/wkq/util/exif/MetadataScrubberTest.kt
- doc/privacy_policy.html
primaryKeyword: 'Limpeza de metadados privados: what it does in CaptionMeta'
relatedPages:
- /
- /support
template: standard-article
---

# Limpeza de metadados privados: what it does in CaptionMeta

Uma fotografia pode conter localização, câmara e outros metadados que não devem ser incluídos em todas as entregas.

## What this feature helps you do

- Inspecionar categorias de metadados EXIF, IPTC e XMP acompanhadas
- Remover metadados privados selecionados de uma cópia processada
- Manter o ficheiro original separado do fluxo de saída limpo

## Where it fits in the workflow

- Selecione a fotografia a inspecionar
- Reveja as categorias disponíveis para limpeza
- Execute a limpeza e use a cópia na entrega

## What to check before export

- Categorias de localização, câmara e outros metadados acompanhados pelo fluxo de limpeza

## What to keep in mind

- A limpeza baseia-se nas categorias implementadas na versão atual; reveja o resultado antes da publicação.

