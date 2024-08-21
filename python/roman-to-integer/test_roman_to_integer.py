import roman_to_integer as ri


def test_extract_portion_to_eval():
    assert ri.extract_portion_to_eval("III") == "I"
    assert ri.extract_portion_to_eval("IV") == "IV"
    assert ri.extract_portion_to_eval("XL") == "XL"
    assert ri.extract_portion_to_eval("CM") == "CM"
    assert ri.extract_portion_to_eval("MC") == "M"
    assert ri.extract_portion_to_eval("XC") == "XC"
    assert ri.extract_portion_to_eval("XIV") == "X"


def test_split_into_portions_to_eval():
    assert ["I", "I", "I"] == ri.split_into_expanded_form("III")
    assert ["X", "IV"] == ri.split_into_expanded_form("XIV")
    # assert ["L", "V", "I", "I", "I"] == ri.split_into_expanded_form("LVIII")
    # assert ["M", "CM", "XC", "IV"] == ri.split_into_expanded_form("MCMXCIV")


def test_numeral_to_integer():
    assert 3 == ri.numeral_to_integer("III")
    assert 58 == ri.numeral_to_integer("LVIII")
    assert 1994 == ri.numeral_to_integer("MCMXCIV")


