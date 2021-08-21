def sum_bytes(bytes):
    bytes_sum = sum(
        [
            int(bytes[0]),
            int(bytes[1]),
            int(bytes[2]),
            int(bytes[3])
        ]
    )
    return bytes_sum


def bytes_to_binary_repr(bytes_):
    ''' Transforma bytes para pra repr. binária '''
    bin_bytes = []
    for byte_ in bytes_:
        int_ = int(byte_)
        bin_bytes.append(format(int_, '08b'))
    return bin_bytes


def binary_repr_to_int(bin_bytes):
    '''Transforma repr. binária pra ints'''
    int_bytes = []
    for bin_ in bin_bytes:
        int_bytes .append(int(bin_, 2))
    return int_bytes


def int_list_to_bytes(int_bytes):
    ''' Transforma ints pra bytes '''
    bytes_ = bytes(int_bytes)
    return bytes_
