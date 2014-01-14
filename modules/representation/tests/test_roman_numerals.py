from ..roman_numerals import convert_to as to_rom, convert_from as from_rom

def test_roman_numerals_to():
    # Basics
    assert to_rom(0) == 'N'
    assert to_rom(1) == 'I'
    assert to_rom(5) == 'V'
    assert to_rom(10) == 'X'
    assert to_rom(50) == 'L'
    assert to_rom(100) == 'C'
    assert to_rom(500) == 'D'
    assert to_rom(1000) == 'M'

    # Simple Composite
    assert to_rom(6) == 'VI'
    assert to_rom(11) == 'XI'
    assert to_rom(51) == 'LI'
    assert to_rom(101) == 'CI'
    assert to_rom(501) == 'DI'
    assert to_rom(530) == 'DXXX'
    assert to_rom(550) == 'DL'
    assert to_rom(1001) == 'MI'
    assert to_rom(7) == 'VII'
    assert to_rom(70) == 'LXX'
    assert to_rom(1800) == 'MDCCC'

    # Subtractive notation
    assert to_rom(4) == 'IV'
    assert to_rom(9) == 'IX'
    assert to_rom(19) == 'XIX'
    assert to_rom(39) == 'XXXIX'
    assert to_rom(40) == 'XL'
    assert to_rom(49) == 'XLIX'
    assert to_rom(90) == 'XC'
    assert to_rom(99) == 'XCIX'

    # Full Composite
    assert to_rom(25) == 'XXV'
    assert to_rom(87) == 'LXXXVII'
    assert to_rom(434) == 'CDXXXIV'
    assert to_rom(1337) == 'MCCCXXXVII'
    assert to_rom(4567) == 'MMMMDLXVII'
    assert to_rom(949) == 'CMXLIX'

    # TODO very large numbers

def test_roman_numerals_from():
    # Basics
    assert from_rom('N') == 0
    assert from_rom('I') == 1
    assert from_rom('V') == 5
    assert from_rom('X') == 10
    assert from_rom('L') == 50
    assert from_rom('C') == 100
    assert from_rom('D') == 500
    assert from_rom('M') == 1000

    # Simple Composite
    assert from_rom('VI') == 6
    assert from_rom('XI') == 11
    assert from_rom('LI') == 51
    assert from_rom('CI') == 101
    assert from_rom('DI') == 501
    assert from_rom('DXXX') == 530
    assert from_rom('DL') == 550
    assert from_rom('MI') == 1001
    assert from_rom('VII') == 7
    assert from_rom('LXX') == 70
    assert from_rom('MDCCC') == 1800

    # Subtractive notation
    assert from_rom('IV') == 4
    assert from_rom('IX') == 9
    assert from_rom('XIX') == 19
    assert from_rom('XXXIX') == 39
    assert from_rom('XL') == 40
    assert from_rom('XLIX') == 49
    assert from_rom('XC') == 90
    assert from_rom('XCIX') == 99

    # Full Composite
    assert from_rom('XXV') == 25
    assert from_rom('LXXXVII') == 87
    assert from_rom('CDXXXIV') == 434
    assert from_rom('MCCCXXXVII') == 1337
    assert from_rom('MMMMDLXVII') == 4567
    assert from_rom('CMXLIX') == 949

    # TODO very large numbers
