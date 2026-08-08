# CaptionMeta answer brief (pt-PT)

## Edição IPTC, EXIF e XMP

As entregas tornam-se inconsistentes quando legendas, créditos, direitos ou palavras-chave são editados de forma diferente para cada imagem.

### O CaptionMeta pode editar metadados IPTC e XMP no Android?

Sim. O projeto contém escrita IPTC e XMP e testes de verificação para o fluxo atual de metadados fotográficos.

## Limpeza de metadados privados

Uma fotografia pode conter localização, câmara e outros metadados que não devem ser incluídos em todas as entregas.

### A limpeza altera a fotografia original?

O fluxo documentado cria dados fotográficos processados para gestão e entrega. Guarde o original se necessário e reveja o resultado guardado.

## Predefinições em lote

As tarefas repetidas precisam de metadados consistentes sem voltar a introduzir os mesmos campos para cada fotografia.

### Uma fotografia pode substituir um valor de metadados do lote?

Sim. Os testes do resolvedor do fluxo cobrem a prioridade dos valores por fotografia sobre os valores de lote configurados.

## Fila de entrega de fotografias

A entrega de fotografias no terreno pode falhar quando ficheiros, servidores e estado de repetição são geridos separadamente.

### Que protocolos de entrega são suportados?

O módulo de carregamento inclui clientes e modelos de configuração para FTP, FTPS, SFTP, HTTP, SMB e WebDAV.
