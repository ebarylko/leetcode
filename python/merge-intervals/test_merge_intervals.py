import merge_intervals as mi


def test_find_overlapping_intervals():
    assert ([(1, 6)], [[8, 10], [15, 18]]) == mi.find_overlapping_interval(([], [[1, 3], [2, 6], [8, 10], [15, 18]]))
    assert ([[1, 3]], []) == mi.find_overlapping_interval(([], [[1, 3]]))
    assert ([[1, 3]], [[4, 6]]) == mi.find_overlapping_interval(([], [[1, 3], [4, 6]]))
    assert ([(1, 5)], []) == mi.find_overlapping_interval(([], [[1, 4], [4, 5]]))


def test_merge_intervals():
    assert [[1, 6], [8, 10], [15, 18]] == mi.merge_intervals([[2, 6], [1, 3], [8, 10], [15, 18]])
    assert [[1, 5]] == mi.merge_intervals([[1, 4],[4, 5]])
    assert [[1, 4]] == mi.merge_intervals([[1, 4]])


def test_find_overlapping_intervals_2():
    assert mi.find_overlapping_interval_2(([], [[1, 3], [2, 6], [8, 10], [15, 18]])) == ([[1, 6]], [[8, 10], [15, 18]])
    assert mi.find_overlapping_interval_2(([], [[1, 3]])) == ([[1, 3]], [])
    assert mi.find_overlapping_interval_2(([], [[1, 3], [4, 6]])) == ([[1, 3]], [[4, 6]])
    assert mi.find_overlapping_interval_2(([], [[1, 4], [4, 5]])) == ([[1, 5]], [])


def test_merge_intervals_2():
    assert [[1, 6], [8, 10], [15, 18]] == mi.merge_intervals_2([[2, 6], [1, 3], [8, 10], [15, 18]])
    assert [[1, 5]] == mi.merge_intervals_2([[1, 4],[4, 5]])
    assert [[1, 4]] == mi.merge_intervals_2([[1, 4]])
