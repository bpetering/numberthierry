from .. import odd

def test_odd():
    assert odd.check(-1) == True
    assert odd.check(0) == False
    assert odd.check(1) == True
    assert odd.check(3.0) == True
    # TODO assert raises - type error
