import optimal_partition as opt


# def test_simple_things():
#     assert 1

def test_unique_substring():
    assert opt.unique_substring([], "s") == ["s"]

# def test_optimal_partition():
#     assert optimal_partition("abacaba") == 4
#     assert optimal_partition("ssssss") == 6
