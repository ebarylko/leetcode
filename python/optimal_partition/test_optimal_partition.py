import optimal_partition as pt


# def test_simple_things():
#     assert 1

def test_unique_substring():
    # assert pt.unique_substring([], "") == [[""], ""]
    # assert pt.unique_substring([], "s") == [["s"], []]
    # assert pt.unique_substring([], "ss") == [["s"], ["s"]]
    # assert pt.unique_substring([], "sts") == [["st"], ["s"]]
    # assert pt.unique_substring([], "stq") == [["stq"], []]
    assert pt.unique_substring(([], "abacaba")) == (["ab"], ['a', 'c', 'a', 'b', 'a'])
    assert pt.unique_substring((["ab"], ['a', 'c', 'a', 'b', 'a'])) == (["ab", "ac"], ['a', 'b', 'a'])


def test_unique_substrings():
    assert pt.unique_substrings("abacaba") == 2

# def test_optimal_partition():
#     assert optimal_partition("abacaba") == 4
#     assert optimal_partition("ssssss") == 6
