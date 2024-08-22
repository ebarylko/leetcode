import merge_intervals as mi

def test_merge_intervals():
    assert mi.merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
    assert mi.merge_intervals([[1, 4],[4, 5]]) == [[1, 5]]