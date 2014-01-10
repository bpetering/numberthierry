from ..roman_numerals import convert_to as to_rom, convert_from as from_rom

def test_roman_numerals_to():
    # TODO 0?
    # Basics
    assert to_rom(1) == 'I'
    assert to_rom(5) == 'V'
    assert to_rom(10) == 'X'
    assert to_rom(50) == 'L'
    assert to_rom(100) == 'C'
    assert to_rom(500) == 'D'
    assert to_rom(1000) == 'M'

    # Subtractive notation
    assert to_rom(3) == 'III'
    assert to_rom(4) == 'IV'
    assert to_rom(9) == 'IX'
    assert to_rom(49) == 'IL'
    assert to_rom(99) == 'IC'
    assert to_rom(499) == 'ID'
    assert to_rom(999) == 'IM'

    # Simple Composite
    assert to_rom(6) == 'VI'
    assert to_rom(11) == 'XI'
    assert to_rom(51) == 'LI'
    assert to_rom(101) == 'CI'
    assert to_rom(501) == 'DI'
    assert to_rom(1001) == 'MI'

    # Full Composite
    assert to_rom(25) == 'XV'
    assert to_rom(87) == 'LXXXVII'
    assert to_rom(434) == 'IDXXXIV'     # TODO ?
    assert to_rom(1337) == 'MCCCVII'
    assert to_rom(4567) == 'MMMMDLXVII'
    assert to_rom(949) == 'IMIL'

def test_roman_numerals_from():
    pass
    # reverse order of above tests
