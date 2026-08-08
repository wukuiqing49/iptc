---
contentId: metadata-editor
locale: pt-PT
status: machine-draft
title: 'Edição IPTC, EXIF e XMP: what it does in CaptionMeta'
description: Reveja e edite legendas, títulos, palavras-chave, autores, direitos de
  autor, direitos e localização. Learn the exact problem, options, verified steps,
  and known limitations.
slug: edição-iptc-exif-e-xmp
intent: feature education
audience: app users
canonical: ''
evidence:
- core/core_exif/src/main/java/com/wkq/util/exif/MetadataScrubber.kt
- core/core_exif/src/test/java/com/wkq/iptc/feature/press/metadata/IptcAndXmpVerificationTest.kt
- feature/feature_app/src/main/res/values/strings.xml
primaryKeyword: 'Edição IPTC, EXIF e XMP: what it does in CaptionMeta'
relatedPages:
- /
- /support.html
template: standard-article
---

# Edição IPTC, EXIF e XMP: what it does in CaptionMeta

As entregas tornam-se inconsistentes quando legendas, créditos, direitos ou palavras-chave são editados de forma diferente para cada imagem.

## What this feature helps you do

- Ler e inspecionar metadados EXIF, IPTC e XMP suportados
- Escrever legendas, títulos, palavras-chave, autores, direitos de autor, direitos e localização em cópias processadas
- Usar valores por fotografia para ajustar ou substituir valores de lote

## Where it fits in the workflow

- Selecione uma fotografia ou um grupo de fotografias locais
- Escolha uma predefinição ou introduza legendas, títulos, palavras-chave, autor e direitos
- Reveja o resultado e guarde a cópia processada

## What to check before export

- Campos IPTC principais e alargados, campos XMP, tratamento EXIF e valores de localização

## What to keep in mind

- Os campos disponíveis e o comportamento de escrita dependem do ficheiro selecionado e dos campos ativados no fluxo.

