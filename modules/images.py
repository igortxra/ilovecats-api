from .bytes import sum_bytes


def save(path, img_name, image_bytes):
    with open(path + img_name, 'wb') as f:
        f.write(image_bytes)


def get(paths, img_name):
    if img_name:
        for path in paths:
            try:
                f = open(path + img_name, 'rb')
                file = f.read()
                f.close()
                return file
            except FileNotFoundError:
                pass


def is_bitmap(img_bytes):
    print(chr(img_bytes[0])+chr(img_bytes[1]))
    return chr(img_bytes[0])+chr(img_bytes[1]) == 'BM'


def bitmap_info(img_bytes):
    size = sum_bytes(img_bytes[2:6])
    pixels_start_byte = sum_bytes(img_bytes[10:14])
    info = {
        'size': size,
        'pixels_start_byte': pixels_start_byte}
    return info
