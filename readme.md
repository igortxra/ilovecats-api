# Ilovecats-API
Essa é uma API que fornece a possibilidade de **uploads e downloads de imagens bitmap** (de gatos, claro). <br>
Há também como esconder mensagens nas imagens, usando esteganografia. <br>
Com a API é possível **escrever e recuperar as mensagens escondidas na imagem.**<br>

## Introducão
- Baixe uma imagem .bmp <a href="http://steve.sourceforge.net/system/goodimage.bmp"> aqui </a> (É um gato, óbvio.)
- Substitua as \<tags\> pelo valor correto. 
- A API suporta somente imagem no formato bitmap (.bmp)

## Como iniciar a API
- Rode o arquivo app.py com o python

## API Methods

### POST /upload
#### Faz upload da imagem no servidor.
```bash
curl -X POST http://localhost:8000/upload -F data=@cat.bmp
```
<hr>

### GET /get-image
#### Baixa uma imagem no servidor (modificadas ou não).
```bash
curl -X GET http://localhost:8000/get-image?q=cat_123.bmp --output normal_cat.bmp
```

<hr>

### POST /write-message-on-image
#### Escreve uma mensagem na imagem especificada.
```bash
# Linux
curl -X POST http://localhost:8000/write-message-on-image \
-H 'Content-Type: application/json' \
-d '{"image_name" : "cat_123.bmp", "message": "Amo gatos!"}'

# Windows
curl -X POST http://localhost:8000/write-message-on-image -H 'Content-Type: application/json' -d "{\"image_name\" : \"cat_616.bmp\", \"message\": \"Amo gatos!\"}"
```
<hr>

### GET /decode-message-from-image
#### Exibe mensagem escondida na imagem especificada.
```bash
curl http://localhost:8000/decode-message-from-image?q=same_cat_123.bmp
```
