---
contentId: metadata-editor
locale: fr-FR
status: machine-draft
title: 'Modification IPTC, EXIF et XMP: what it does in CaptionMeta'
description: Vérifiez et modifiez les légendes, titres, mots-clés, auteurs, droits
  d’auteur, droits et lieux. Learn the exact problem, options, verified steps, and
  known limitations.
slug: modification-iptc-exif-et-xmp
intent: feature education
audience: app users
canonical: ''
evidence:
- core/core_exif/src/main/java/com/wkq/util/exif/MetadataScrubber.kt
- core/core_exif/src/test/java/com/wkq/iptc/feature/press/metadata/IptcAndXmpVerificationTest.kt
- feature/feature_app/src/main/res/values/strings.xml
primaryKeyword: 'Modification IPTC, EXIF et XMP: what it does in CaptionMeta'
relatedPages:
- /
- /support.html
template: standard-article
---

# Modification IPTC, EXIF et XMP: what it does in CaptionMeta

Les livraisons deviennent incohérentes lorsque les légendes, crédits, droits ou mots-clés sont modifiés différemment pour chaque image.

## What this feature helps you do

- Lire et inspecter les métadonnées EXIF, IPTC et XMP prises en charge
- Écrire les légendes, titres, mots-clés, auteurs, droits d’auteur, droits et lieux dans des copies traitées
- Utiliser des valeurs par photo pour préciser ou remplacer les valeurs du lot

## Where it fits in the workflow

- Sélectionner une photo ou un groupe de photos locales
- Choisir un préréglage ou saisir les légendes, titres, mots-clés, auteurs et droits
- Vérifier le résultat et enregistrer la copie traitée

## What to check before export

- Champs IPTC principaux et étendus, champs XMP, traitement EXIF et valeurs de lieu

## What to keep in mind

- Les champs disponibles et le comportement d’écriture dépendent du fichier choisi et des champs activés dans le flux.

