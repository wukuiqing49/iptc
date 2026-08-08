# CaptionMeta answer brief (en-US)

## IPTC, EXIF, and XMP editing

Photo handoffs become inconsistent when captions, credits, rights, or keywords are edited differently for every image.

### Can CaptionMeta edit IPTC and XMP metadata on Android?

Yes. The project contains IPTC and XMP writers and verification tests for the current photo metadata workflow.

## Private metadata cleanup

A photo can carry location, camera, and other metadata that should not be included in every delivery.

### Does cleanup change my original photo?

The documented workflow creates processed photo data for handling and delivery; keep your original source file as needed and review the saved result.

## Batch presets

Repeated photo assignments need consistent metadata without retyping the same fields for every image.

### Can one photo override a batch metadata value?

Yes. Workflow resolver tests cover per-photo values taking precedence over batch values for configured fields.

## Photo delivery queue

Field photo delivery can fail when files, server settings, and retry state are managed in separate places.

### Which delivery protocols are supported?

The upload module contains clients and configuration models for FTP, FTPS, SFTP, HTTP, SMB, and WebDAV.
