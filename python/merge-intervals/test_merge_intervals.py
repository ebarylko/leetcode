import merge_intervals as mi


def test_find_overlapping_intervals():
    assert ([(1, 6)], [[8, 10], [15, 18]]) == mi.find_overlapping_interval(([], [[1, 3], [2, 6], [8, 10], [15, 18]]))
    assert ([[1, 3]], []) == mi.find_overlapping_interval(([], [[1, 3]]))
    assert ([[1, 3]], [[4, 6]]) == mi.find_overlapping_interval(([], [[1, 3], [4, 6]]))
    assert ([(1, 5)], []) == mi.find_overlapping_interval(([], [[1, 4], [4, 5]]))


def test_merge_intervals():
    assert mi.merge_intervals([[2, 6], [1, 3], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
    assert mi.merge_intervals([[1, 4],[4, 5]]) == [[1, 5]]