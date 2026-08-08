---
contentId: batch-presets
locale: fr-FR
status: machine-draft
title: 'Préréglages par lot: what it does in CaptionMeta'
description: Réutilisez des préréglages IPTC sur plusieurs photos tout en conservant
  les remplacements individuels. Learn the exact problem, options, verified steps,
  and known limitations.
slug: préréglages-par-lot
intent: feature education
audience: app users
canonical: ''
evidence:
- core/core_exif/src/test/java/com/wkq/iptc/feature/press/model/MetadataTemplateWorkflowTest.kt
- feature/feature_app/src/test/java/com/wkq/iptc/feature/press/workflow/WorkflowResolverTest.kt
- feature/feature_app/src/main/res/values/strings.xml
primaryKeyword: 'Préréglages par lot: what it does in CaptionMeta'
relatedPages:
- /
- /support.html
template: standard-article
---

# Préréglages par lot: what it does in CaptionMeta

Les travaux répétés deviennent difficiles à maintenir de façon cohérente lorsque les mêmes champs sont saisis pour chaque photo.

## What this feature helps you do

- Créer et réutiliser des modèles ou préréglages de métadonnées
- Appliquer des valeurs de lot à plusieurs photos sélectionnées
- Remplacer une valeur pour une photo qui nécessite une légende ou un champ différent

## Where it fits in the workflow

- Choisir ou créer un préréglage IPTC
- Sélectionner les champs et les photos à traiter
- Vérifier les remplacements par photo et écrire les valeurs finales

## What to check before export

- Champs du préréglage, valeurs de lot, remplacements par photo, auteur, lieu et paramètres de livraison

## What to keep in mind

- Un préréglage agit uniquement sur les champs configurés pour le flux ; les champs vides ou désactivés ne sont pas considérés comme renseignés.

