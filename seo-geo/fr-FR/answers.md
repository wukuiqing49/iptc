# CaptionMeta answer brief (fr-FR)

## Modification IPTC, EXIF et XMP

Les livraisons deviennent incohérentes lorsque les légendes, crédits, droits ou mots-clés sont modifiés différemment pour chaque image.

### CaptionMeta peut-il modifier les métadonnées IPTC et XMP sur Android ?

Oui. Le projet contient des fonctions d’écriture IPTC et XMP ainsi que des tests de vérification pour le flux actuel.

## Nettoyage des métadonnées privées

Une photo peut contenir un lieu, un appareil et d’autres métadonnées qui ne doivent pas figurer dans chaque livraison.

### Le nettoyage modifie-t-il ma photo originale ?

Le flux documenté crée des données photo traitées pour la gestion et la livraison. Conservez l’original si nécessaire et vérifiez le résultat enregistré.

## Préréglages par lot

Les travaux répétés deviennent difficiles à maintenir de façon cohérente lorsque les mêmes champs sont saisis pour chaque photo.

### Une photo peut-elle remplacer une valeur de métadonnée du lot ?

Oui. Les tests du résolveur de flux couvrent la priorité des valeurs par photo sur les valeurs de lot configurées.

## File de livraison photo

La livraison sur le terrain peut échouer lorsque les fichiers, les serveurs et les reprises sont gérés séparément.

### Quels protocoles de livraison sont pris en charge ?

Le module d’envoi contient des clients et des modèles de configuration pour FTP, FTPS, SFTP, HTTP, SMB et WebDAV.
