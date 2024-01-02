import kth_factor_of_n as kth


def test_generate_positive_integers_up_to_square_root():
    assert kth.generate_positive_integers_up_to_square_root(12) == [1, 2, 3]
    assert kth.generate_positive_integers_up_to_square_root(1) == [1]
    assert kth.generate_positive_integers_up_to_square_root(16) == [1, 2, 3, 4]


def test_quotient_divisor_and_power():
    assert kth.quotient_divisor_and_power((4, 2, 0)) == (2, 2, 1)
    assert kth.quotient_divisor_and_power((3, 2, 0)) == (1.5, 2, 1)


def test_find_factors_of_n_using_t():
    assert kth.find_factors_of_n_using_t(10, 1) == {1, 10}
    assert kth.find_factors_of_n_using_t(16, 3) == {1, 16}
    assert kth.find_factors_of_n_using_t(16, 2) == {1, 2, 4, 8, 16}
    assert kth.find_factors_of_n_using_t(12, 2) == {1, 2, 3, 4, 6, 12}



def test_kth_factor():
    assert kth.kth_factor(12, 3) == 3
    # assert kth.kth_factor(7, 2) == 7
    # assert kth.kth_factor(4, 4) == -1


