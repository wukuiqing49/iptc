---
contentId: photo-delivery
locale: fr-FR
status: machine-draft
title: 'File de livraison photo: what it does in CaptionMeta'
description: Mettez les photos traitées en file, livrez-les via des serveurs configurés
  et vérifiez les résultats. Learn the exact problem, options, verified steps, and
  known limitations.
slug: file-de-livraison-photo
intent: feature education
audience: app users
canonical: ''
evidence:
- core/core_upload/src/main/java/com/wkq/iptc/upload/UploadDispatcher.kt
- core/core_upload/src/main/java/com/wkq/iptc/upload/http/RetryInterceptor.kt
- core/core_upload/consumer-rules.pro
primaryKeyword: 'File de livraison photo: what it does in CaptionMeta'
relatedPages:
- /
- /support
template: standard-article
---

# File de livraison photo: what it does in CaptionMeta

La livraison sur le terrain peut échouer lorsque les fichiers, les serveurs et les reprises sont gérés séparément.

## What this feature helps you do

- Mettre les fichiers photo traités en file de livraison
- Prendre en charge les clients FTP, FTPS, SFTP, HTTP, SMB et WebDAV configurés
- Réessayer certains échecs HTTP temporaires et conserver les résultats des tâches

## Where it fits in the workflow

- Configurer un profil de serveur de livraison
- Choisir les photos traitées et les ajouter à la file
- Surveiller la file, relancer les échecs admissibles et consulter l’historique

## What to check before export

- Profils de serveurs FTP, FTPS, SFTP, HTTP, SMB et WebDAV

## What to keep in mind

- La livraison nécessite un serveur accessible et des identifiants configurés par l’utilisateur. L’application ne fournit pas de stockage photo hébergé.

