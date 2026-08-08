---
contentId: privacy-cleanup
locale: fr-FR
status: machine-draft
title: 'Nettoyage des métadonnées privées: what it does in CaptionMeta'
description: Inspectez et supprimez certaines données EXIF, IPTC et XMP avant de partager
  une copie traitée. Learn the exact problem, options, verified steps, and known limitations.
slug: nettoyage-des-métadonnées-privées
intent: feature education
audience: app users
canonical: ''
evidence:
- core/core_exif/src/main/java/com/wkq/util/exif/MetadataScrubber.kt
- core/core_exif/src/test/java/com/wkq/util/exif/MetadataScrubberTest.kt
- doc/privacy_policy.html
primaryKeyword: 'Nettoyage des métadonnées privées: what it does in CaptionMeta'
relatedPages:
- /
- /support.html
template: standard-article
---

# Nettoyage des métadonnées privées: what it does in CaptionMeta

Une photo peut contenir un lieu, un appareil et d’autres métadonnées qui ne doivent pas figurer dans chaque livraison.

## What this feature helps you do

- Inspecter les catégories EXIF, IPTC et XMP suivies
- Supprimer certaines métadonnées privées d’une copie photo traitée
- Séparer le fichier original du flux de sortie nettoyé

## Where it fits in the workflow

- Sélectionner la photo à inspecter
- Examiner les catégories de métadonnées disponibles pour le nettoyage
- Lancer le nettoyage et utiliser la copie pour la livraison

## What to check before export

- Catégories de lieu, d’appareil et autres métadonnées suivies par le flux de nettoyage

## What to keep in mind

- Le nettoyage dépend des catégories implémentées dans la version actuelle ; vérifiez la sortie avant publication.

