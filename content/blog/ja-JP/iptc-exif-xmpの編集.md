---
contentId: metadata-editor
locale: ja-JP
status: machine-draft
title: 'IPTC、EXIF、XMPの編集: what it does in CaptionMeta'
description: キャプション、見出し、キーワード、署名、著作権、権利、位置情報を確認・編集します。 Learn the exact problem, options,
  verified steps, and known limitations.
slug: iptc-exif-xmpの編集
intent: feature education
audience: app users
canonical: ''
evidence:
- core/core_exif/src/main/java/com/wkq/util/exif/MetadataScrubber.kt
- core/core_exif/src/test/java/com/wkq/iptc/feature/press/metadata/IptcAndXmpVerificationTest.kt
- feature/feature_app/src/main/res/values/strings.xml
primaryKeyword: 'IPTC、EXIF、XMPの編集: what it does in CaptionMeta'
relatedPages:
- /
- /support.html
template: standard-article
---

# IPTC、EXIF、XMPの編集: what it does in CaptionMeta

写真ごとにキャプション、クレジット、権利、キーワードを別々に編集すると、納品内容が不統一になります。

## What this feature helps you do

- 対応するEXIF、IPTC、XMPメタデータを読み取り確認する
- キャプション、見出し、キーワード、署名、著作権、権利、位置情報を書き込む
- 写真ごとの値で一括値を細かく調整または上書きする

## Where it fits in the workflow

- 写真を1枚または複数選択する
- プリセットを選ぶか、キャプション、見出し、キーワード、署名、権利情報を入力する
- 結果を確認して処理済みコピーを保存する

## What to check before export

- IPTCコア・拡張項目、XMP項目、EXIF処理、位置情報

## What to keep in mind

- 利用できる項目と書き込み動作は、選択したファイルとワークフローで有効な項目によって異なります。

