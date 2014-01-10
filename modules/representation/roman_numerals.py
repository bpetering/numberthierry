class RomanNumerals(object):
    @classmethod
    def convert(cls, n):
        out = ''
        numerals = [('M', 1000), ('D', 500), ('C', 100), ('L', 50), ('X', 10), ('V', 5), ('I', 1)]
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
                    if x == 1 and test_n == 4:
                        out += 'IV'
                    else:
                        out += letter * (test_n / x)
        return out


# TODO method for converting FROM representations, so we can be clever and specify
# things however?

# TODO meta info interface: e.g. number of characters in representation. where?


# TODO unit tests this file first
