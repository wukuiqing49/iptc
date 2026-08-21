---
contentId: photo-delivery
locale: es-419
status: machine-draft
title: 'Cola de entrega de fotos: what it does in CaptionMeta'
description: Pon fotos procesadas en cola, entrégalas mediante servidores configurados
  y revisa los resultados. Learn the exact problem, options, verified steps, and known
  limitations.
slug: cola-de-entrega-de-fotos
intent: feature education
audience: app users
canonical: ''
evidence:
- core/core_upload/src/main/java/com/wkq/iptc/upload/UploadDispatcher.kt
- core/core_upload/src/main/java/com/wkq/iptc/upload/http/RetryInterceptor.kt
- core/core_upload/consumer-rules.pro
primaryKeyword: 'Cola de entrega de fotos: what it does in CaptionMeta'
relatedPages:
- /
- /support
template: standard-article
---

# Cola de entrega de fotos: what it does in CaptionMeta

La entrega de fotos de campo puede fallar cuando los archivos, la configuración del servidor y los reintentos se gestionan por separado.

## What this feature helps you do

- Poner archivos procesados en una cola de entrega
- Usar clientes configurados de FTP, FTPS, SFTP, HTTP, SMB y WebDAV
- Reintentar algunos fallos HTTP temporales y conservar los resultados de las tareas

## Where it fits in the workflow

- Configura un perfil de servidor de entrega
- Elige fotos procesadas y añádelas a la cola
- Supervisa la cola, reintenta fallos aptos y revisa el historial

## What to check before export

- Perfiles de servidor FTP, FTPS, SFTP, HTTP, SMB y WebDAV

## What to keep in mind

- La entrega requiere un servidor accesible y credenciales configuradas por el usuario. La aplicación no ofrece almacenamiento fotográfico alojado.

