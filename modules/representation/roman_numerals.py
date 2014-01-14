numerals = [('M', 1000), ('D', 500), ('C', 100), ('L', 50), ('X', 10), ('V', 5), ('I', 1), ('N', 0)]

def is_subtractive(arg):
    if type(arg) is tuple:
        return arg[1] in [1000,100,10,1]
    if type(arg) is int:
        return arg in [1000,100,10,1]
    if type(arg) is str or type(arg) is unicode:
        return arg in ['M', 'C', 'X', 'I']
    raise Exception('bad type for is_subtractive() arg: {}'.format(type(arg)))

# Get next 1-val from numerals, skipping current pos usually
def next_1val(cur_pos):
    if cur_pos == 6:
        return 6
    i = cur_pos + 1
    l_n = len(numerals)
    while i < l_n and str(numerals[i][1])[0] != '1':
        i += 1
    return i

def convert_to(n):
    out = ''

    if n < 0:
        raise Exception('tried to convert negative integer to roman numerals')

    # Special-case 0
    if n == 0:
        return numerals[-1][0]

    # Iterate manually with index. Don't always advance on each iteration,
    # example case 20 == 'XX'
    i = 0
    while True:
        while numerals[i][1] > n:
            i += 1
        (letter, value) = numerals[i]

        # print "i: {}".format(i)
        # print "letter: {}".format(letter)
        # print "value: {}".format(value)

        # If there's a previous value we skipped, first try that with
        # subtractive notation
        # CMXLIX
        if i > 0:
            #print "trying subtractive notation"
            back_index = i-1
            (prev_letter, prev_value) = numerals[back_index]
            (subtractive_letter, subtractive_value) = numerals[ next_1val(back_index) ]
            test_value = prev_value - subtractive_value
            # print "prev_value: {}".format(prev_value)
            # print "subtractive_value: {}".format(subtractive_value)
            # print "test_value: {}".format(test_value)
            if n >= test_value:
                out += subtractive_letter + prev_letter
                n -= test_value
                if n == 0: break
                continue

        # print "n = {}".format(n)
        # print "value = {}".format(value)

        # Otherwise subtract the highest possible multiple of this letter's value
        value_mult = value
        while value_mult <= n:
            value_mult += value
        if value_mult > n:
            value_mult -= value     # adjust back <=
        out += letter * (value_mult / value)
        n -= value_mult
        if n == 0:
            break

    assert(n == 0)      # should never finish with n > 0
    return out

def convert_from(roman):
    # TODO handle bogus XXXX as 40?
    table = {
        'M':    1000,
        'CM':   900,
        'D':    500,
        'CD':   400,
        'C':    100,
        'XC':   90,
        'L':    50,
        'XL':   40,
        'X':    10,
        'IX':   9,
        'V':    5,
        'IV':   4,
        'I':    1,
        'N':    0
    }
    n = 0
    i = len(roman) - 1
    while i >= 0:
        # Check if previous letter is subtractive - if not, add its value
        token = roman[i]
        if i > 0 and roman[i] != roman[i-1] and table[roman[i-1]] < table[roman[i]] and is_subtractive(roman[i-1]):
            token = roman[i-1] + token
            i -= 1
        n += table[token]
        i -= 1
    return n


# import sys
# print convert_from(sys.argv[1])


# TODO meta info interface: e.g. number of characters in representation. where?
