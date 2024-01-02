import kth_factor_of_n as kth


def test_generate_positive_integers_up_to_square_root():
    assert kth.generate_positive_integers_up_to_square_root(12) == [1, 2, 3]
    assert kth.generate_positive_integers_up_to_square_root(1) == [1]
    assert kth.generate_positive_integers_up_to_square_root(16) == [1, 2, 3, 4]


def test_kth_factor():
    assert kth.kth_factor(12, 3) == 3
    assert kth.kth_factor(7, 2) == 7
    assert kth.kth_factor(4, 4) == -1
