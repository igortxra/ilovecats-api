def sum_bytes(bytes):
    """ Sum 4 bytes """

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
    ''' Transform bytes to binary representation '''

    bin_bytes = []
    for byte_ in bytes_:
        int_ = int(byte_)
        bin_bytes.append(format(int_, '08b'))
    return bin_bytes


def binary_repr_to_int(bin_bytes):
    ''' Transform binary representations to int '''

    int_bytes = []
    for bin_ in bin_bytes:
        int_bytes .append(int(bin_, 2))
    return int_bytes


def int_list_to_bytes(int_bytes):
    ''' Transform ints to bytes '''

    bytes_ = bytes(int_bytes)
    return bytes_
