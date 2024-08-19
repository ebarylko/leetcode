import roman_to_integer as ri


def test_numeral_to_integer():
    assert 3 == ri.numeral_to_integer("III")
    assert 58 == ri.numeral_to_integer("LVIII")
    assert 1994 == ri.numeral_to_integer("MCMXCIV")

