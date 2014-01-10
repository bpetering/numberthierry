
def convert_to(n):
    out = ''
    numerals = [('M', 1000), ('D', 500), ('C', 100), ('L', 50), ('X', 10), ('V', 5), ('I', 1), ('N', 0)]
    # TODO nyi subtractive notation
    while n > 0:
        for test in numerals:
            letter = test[0]
            x = test[1]
            test_n = x
            while test_n <= n:
                test_n += x
            test_n -= x
            if n >= test_n:
                n -= test_n
                actual_n = test_n / x
                if x == 1 and test_n == 4:  # TODO fully general sub not
                    out += 'IV'
                else:
                    out += letter * (test_n / x)
    return out

def convert_from(n):
    pass


# TODO meta info interface: e.g. number of characters in representation. where?
