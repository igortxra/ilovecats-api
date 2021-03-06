from modules.steganografy import apply_steganografy, decode_steganografy
from modules.helpers import generate_filename, json_message
from config import IMAGES_DIR, STEGO_DIR
import modules.images as img
import server


def upload_image(image_bytes: bytes):
    """ Write image bytes on a file """

    if not img.is_bitmap(image_bytes):
        return 400, json_message('Invalid image format. Upload a .bmp file')

    filename = generate_filename('cat')
    img.save('temp/images/', filename, image_bytes)

    return 200, json_message(filename, 'filename')


def get_image(image_name):
    ''' Search image by name and returns image bytes if found '''

    image_bytes = img.get([IMAGES_DIR, STEGO_DIR], image_name)
    if image_bytes:
        return 200, image_bytes

    return 404, json_message('Image not found')


def write_message_on_image(adict):
    """ Writes given message inner a image with steganografy """

    if 'image_name' not in adict \
            or 'message' not in adict:
        return 400, json_message('Missing image name or message')

    image_name = adict['image_name']

    image_bytes = img.get([IMAGES_DIR], image_name)
    if not image_bytes:
        return 404, json_message('Image specified not found')

    message = adict['message']
    message += '.' if message[-1] != '.' else ''

    applied, message = \
        apply_steganografy(image_bytes, image_name, msg=message)

    if not applied:
        return 400, json_message(message)

    return 200, json_message(message, 'filename')


def decode_message_from_image(image_name):
    """ Return message hidden on the image. """

    image_bytes = img.get([STEGO_DIR], image_name)
    if image_bytes:
        message = decode_steganografy(image_bytes)
        return 200, json_message(message, 'message')

    return 404, json_message('Image not found')
