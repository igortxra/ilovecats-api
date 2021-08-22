from .bytes import sum_bytes


def save(path, img_name, image_bytes):
    ''' Write image bytes on file '''
    with open(path + img_name, 'wb') as f:
        f.write(image_bytes)


def get(paths, img_name):
    ''' Get image bytes'''
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
    ''' Verify is a image is bitmap '''

    return chr(img_bytes[0])+chr(img_bytes[1]) == 'BM'


def bitmap_info(img_bytes):
    ''' Extract bitmap image information '''

    size = sum_bytes(img_bytes[2:6])
    pixels_start_byte = sum_bytes(img_bytes[10:14])
    usable_bytes = size - pixels_start_byte
    info = {
        'size': size,
        'pixels_start_byte': pixels_start_byte,
        'usable_bytes': usable_bytes}
    return info
