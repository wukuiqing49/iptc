---
contentId: photo-delivery
locale: pt-PT
status: machine-draft
title: 'Fila de entrega de fotografias: what it does in CaptionMeta'
description: Coloque fotografias processadas em fila, envie-as através de servidores
  configurados e reveja os resultados. Learn the exact problem, options, verified
  steps, and known limitations.
slug: fila-de-entrega-de-fotografias
intent: feature education
audience: app users
canonical: ''
evidence:
- core/core_upload/src/main/java/com/wkq/iptc/upload/UploadDispatcher.kt
- core/core_upload/src/main/java/com/wkq/iptc/upload/http/RetryInterceptor.kt
- core/core_upload/consumer-rules.pro
primaryKeyword: 'Fila de entrega de fotografias: what it does in CaptionMeta'
relatedPages:
- /
- /support
template: standard-article
---

# Fila de entrega de fotografias: what it does in CaptionMeta

A entrega de fotografias no terreno pode falhar quando ficheiros, servidores e estado de repetição são geridos separadamente.

## What this feature helps you do

- Colocar ficheiros processados numa fila de entrega
- Suportar clientes configurados de FTP, FTPS, SFTP, HTTP, SMB e WebDAV
- Repetir algumas falhas HTTP temporárias e guardar resultados das tarefas

## Where it fits in the workflow

- Configure um perfil de servidor de entrega
- Escolha fotografias processadas e adicione-as à fila
- Monitorize a fila, repita falhas elegíveis e reveja o histórico

## What to check before export

- Perfis de servidor FTP, FTPS, SFTP, HTTP, SMB e WebDAV

## What to keep in mind

- A entrega requer um servidor acessível e credenciais configuradas pelo utilizador. A aplicação não fornece armazenamento fotográfico alojado.

