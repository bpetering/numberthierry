def convert_to(n):
    return hex(n)[2:]

def convert_from(hexadecimal):
    return int(hexadecimal, base=16)
