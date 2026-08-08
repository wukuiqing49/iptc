---
contentId: batch-presets
locale: pt-PT
status: machine-draft
title: 'Predefinições em lote: what it does in CaptionMeta'
description: Reutilize predefinições IPTC num grupo de fotografias mantendo substituições
  por fotografia. Learn the exact problem, options, verified steps, and known limitations.
slug: predefinições-em-lote
intent: feature education
audience: app users
canonical: ''
evidence:
- core/core_exif/src/test/java/com/wkq/iptc/feature/press/model/MetadataTemplateWorkflowTest.kt
- feature/feature_app/src/test/java/com/wkq/iptc/feature/press/workflow/WorkflowResolverTest.kt
- feature/feature_app/src/main/res/values/strings.xml
primaryKeyword: 'Predefinições em lote: what it does in CaptionMeta'
relatedPages:
- /
- /support.html
template: standard-article
---

# Predefinições em lote: what it does in CaptionMeta

As tarefas repetidas precisam de metadados consistentes sem voltar a introduzir os mesmos campos para cada fotografia.

## What this feature helps you do

- Criar e reutilizar modelos ou predefinições de metadados
- Aplicar valores de lote a várias fotografias selecionadas
- Usar substituições por fotografia quando uma imagem precisa de outra legenda ou campo

## Where it fits in the workflow

- Escolha ou crie uma predefinição IPTC
- Selecione os campos e fotografias a processar
- Reveja as substituições e escreva os valores finais

## What to check before export

- Campos da predefinição, valores de lote, substituições por fotografia, autor, localização e definições de entrega

## What to keep in mind

- Uma predefinição só afeta os campos configurados para esse fluxo; campos vazios ou desativados não são considerados preenchidos.

