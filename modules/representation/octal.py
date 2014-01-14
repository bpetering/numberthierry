def convert_to(n):
    return oct(n)[1:]

def convert_from(octal):
    return int(octal, base=8)
