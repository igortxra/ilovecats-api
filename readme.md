### Introduction
- Download a bmp image <a href="http://steve.sourceforge.net/system/goodimage.bmp"> here </a> (its a cat)
- Substitua as \<tags\> pelo valor correto. | Replace tags \<tags\> by correct value.


## API Methods

### POST /upload
```bash
curl -X POST http://localhost:8000/upload \
-F data=@cat.bmp 
```

### GET /get-image
```
curl -X GET http://localhost:8000/get-image?q=<image-name> --output normal_cat.bmp
```

### POST /write-message-on-image
```bash
curl -X POST http://localhost:8000/write-message-on-image \
-H 'Content-Type: application/json' \
-d '{"image_name" : "<image-name>", "message": "<message>"}'
```

### GET/decode-message-from-image
```bash
curl http://localhost:8000/decode-message-from-image?q=<image-name>
```

### GET /get-image (modified one)
```bash
curl http://localhost:8000/get-image?q=<image-name> --output stego_cat.bmp
```