def to_byte(data):
    return b"%02X" % data


def compute_checksum(data):
    return sum(data) & 0xFF


def byte_compute_checksum(data):
    return to_byte(compute_checksum(data))
