from config import STEGO_DIR
from .bytes import binary_repr_to_int, int_list_to_bytes, bytes_to_binary_repr
import modules.images as img


def string_to_binary_representation(string):
    ''' Convert a normal string to binary representation '''

    return ''.join(format(ord(l), 'b').zfill(8)
                   for l in string)


def message_on_lsb_bits(bin_bytes, msg, start):
    ''' Change the LSB from each byte in order to write msg bits '''

    size_msg = len(msg)
    for i in range(size_msg):
        bin_bytes[start + i] = bin_bytes[start + i][:-1] + msg[i]


def apply_steganografy(image_bytes, image_name, msg):
    ''' Process image info and apply steganografy '''

    # Validating image and message
    if not img.is_bitmap(image_bytes):
        return (False, 'Image must be a .bmp')

    msg = string_to_binary_representation(msg)
    img_info = img.bitmap_info(image_bytes)
    if img_info['usable_bytes'] < len(msg):
        return (False, 'Message too large for this image.')

     # Writing message on image
    bin_repr = bytes_to_binary_repr(image_bytes)
    message_on_lsb_bits(bin_repr, msg, img_info['pixels_start_byte'])
    int_bytes = binary_repr_to_int(bin_repr)
    new_img_bytes = int_list_to_bytes(int_bytes)

    # Saving stego image
    filename = f"same_{image_name}"
    img.save(STEGO_DIR, filename, new_img_bytes)

    return (True, filename)


def decode_steganografy(img_bytes):
    ''' Recover a message from a stego image '''

    start_byte = img.bitmap_info(img_bytes)['pixels_start_byte']
    bin_bytes = bytes_to_binary_repr(img_bytes)

    message = ''
    msg_byte = ''

    for byte in bin_bytes[start_byte:]:
        msg_byte += str(byte[-1])

        if len(msg_byte) == 8:
            message += chr(int(msg_byte, 2))
            msg_byte = ''
            if message[-1] == '.':
                break
    return message
