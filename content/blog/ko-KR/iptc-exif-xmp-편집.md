---
contentId: metadata-editor
locale: ko-KR
status: machine-draft
title: 'IPTC, EXIF, XMP 편집: what it does in CaptionMeta'
description: 캡션, 제목, 키워드, 작성자, 저작권, 권리와 위치 메타데이터를 확인하고 편집합니다. Learn the exact problem,
  options, verified steps, and known limitations.
slug: iptc-exif-xmp-편집
intent: feature education
audience: app users
canonical: ''
evidence:
- core/core_exif/src/main/java/com/wkq/util/exif/MetadataScrubber.kt
- core/core_exif/src/test/java/com/wkq/iptc/feature/press/metadata/IptcAndXmpVerificationTest.kt
- feature/feature_app/src/main/res/values/strings.xml
primaryKeyword: 'IPTC, EXIF, XMP 편집: what it does in CaptionMeta'
relatedPages:
- /
- /support
template: standard-article
---

# IPTC, EXIF, XMP 편집: what it does in CaptionMeta

사진마다 캡션, 크레딧, 권리 또는 키워드를 다르게 편집하면 전달 내용이 일관되지 않을 수 있습니다.

## What this feature helps you do

- 지원되는 EXIF, IPTC, XMP 메타데이터를 읽고 확인하기
- 캡션, 제목, 키워드, 작성자, 저작권, 권리와 위치 필드를 처리한 사진 사본에 쓰기
- 사진별 값으로 일괄 값을 세밀하게 조정하거나 재정의하기

## Where it fits in the workflow

- 사진 한 장 또는 여러 장을 선택합니다
- 프리셋을 선택하거나 캡션, 제목, 키워드, 작성자와 권리 정보를 입력합니다
- 결과를 확인하고 처리된 사본을 저장합니다

## What to check before export

- IPTC 기본·확장 필드, XMP 필드, EXIF 처리와 위치 값

## What to keep in mind

- 사용 가능한 필드와 기록 동작은 선택한 파일과 작업 흐름에서 활성화한 필드에 따라 달라집니다.

