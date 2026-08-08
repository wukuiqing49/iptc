# CaptionMeta answer brief (es-419)

## Edición IPTC, EXIF y XMP

Las entregas se vuelven inconsistentes cuando los pies de foto, créditos, derechos o palabras clave se editan de manera distinta para cada imagen.

### ¿CaptionMeta puede editar metadatos IPTC y XMP en Android?

Sí. El proyecto contiene escritura IPTC y XMP y pruebas de verificación para el flujo actual de metadatos fotográficos.

## Limpieza de metadatos privados

Una foto puede incluir ubicación, cámara y otros metadatos que no deberían estar en cada entrega.

### ¿La limpieza cambia mi foto original?

El flujo documentado crea datos fotográficos procesados para gestionar y entregar. Conserva el original si lo necesitas y revisa el resultado guardado.

## Ajustes preestablecidos por lote

Los trabajos repetidos necesitan metadatos consistentes sin volver a escribir los mismos campos para cada foto.

### ¿Una foto puede reemplazar un valor de metadatos del lote?

Sí. Las pruebas del resolutor de flujo cubren la prioridad de los valores por foto sobre los valores por lote configurados.

## Cola de entrega de fotos

La entrega de fotos de campo puede fallar cuando los archivos, la configuración del servidor y los reintentos se gestionan por separado.

### ¿Qué protocolos de entrega son compatibles?

El módulo de carga incluye clientes y modelos de configuración para FTP, FTPS, SFTP, HTTP, SMB y WebDAV.
