def convert_to(n):
    # Python prefixes are stripped for consistency with non-Python formats
    return bin(n)[2:]

def convert_from(binary):
    return int(binary, base=2)
