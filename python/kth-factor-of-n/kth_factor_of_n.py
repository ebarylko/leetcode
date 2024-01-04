import math

import toolz as tz
import itertools as it
import operator as op


def generate_positive_integers_up_to_square_root(number):
    """
    :param number: a positive integer
    :return: a collection of positive integers less than or equal to
    the square root of number
    """
    return tz.thread_last(
        number,
        math.sqrt,
        math.floor,
        (op.add, 1),
        range,
        (tz.drop, 1),
        list)


def quotient_divisor_and_power(t):
    """
    :param t: a tuple containing a quotient, a divisor, and the exponent of the divisor
    :return: a tuple containing the quotient divided by the divisor, the divisor, and the exponent incremented
    """
    quotient, divisor, exponent = t
    return quotient / divisor, divisor, exponent + 1


def find_factors_of_n_using_t(number, divisor):
    """
    :param number: a positive integer
    :param divisor: a positive integer
    :return: a collection of all the integer factors of number that appear
    after continuously dividing by divisor
    """
    return {1, number} if divisor == 1 or number % divisor != 0 else tz.thread_last(
        (number, divisor, 0),
        (tz.iterate, quotient_divisor_and_power),
        (it.takewhile, lambda t: t[0] - int(t[0]) == 0),
        (map, tz.juxt(
            tz.compose(int, tz.first),
            tz.compose(int,
                       tz.partial(math.pow, divisor),
                       tz.last))),
        lambda coll: it.chain(*coll),
        set
    )


def kth_factor(number, k):
    """
    :param number: a positive integer
    :param k: a positive integer
    :return: the kth factor of number if there are at least k factors, -1 otherwise
    ex: kth_factor(10, 3) = 5
    """
    return tz.thread_last(
        number,
        generate_positive_integers_up_to_square_root,
        (tz.mapcat, tz.partial(find_factors_of_n_using_t, number)),
        tz.frequencies,
        list,
        sorted,
        lambda coll: tz.get(k - 1, coll, -1),
    )


def generate_positive_integers_up_to_square_root_2(number):
    """
    :param number: a positive integer
    :return: a collection of positive integers less than or equal to
    the square root of number
    """
    integer_root = math.floor(math.sqrt(number))
    integers = range(1, integer_root + 1)
    return list(integers)


def quotient_divisor_and_power_2(t):
    """
    :param t: a tuple containing a quotient, a divisor, and the exponent of the divisor
    :return: a tuple containing the quotient divided by the divisor, the divisor, and the exponent incremented
    """
    quotient, divisor, exponent = t
    return quotient / divisor, divisor, exponent + 1


def find_factors_of_n_using_t_2(number, divisor):
    """
    :param number: a positive integer
    :param divisor: a positive integer
    :return: a collection of all the integer factors of number that appear
    after continuously dividing by divisor
    """
    if divisor == 1 or number % divisor != 0:
        return {1, number}
    else:
        factors = {1, number}
        t = (number, divisor, 0)
        quotient, divisor, exponent = quotient_divisor_and_power(t)
        while int(quotient) - quotient == 0:
            factors.add(quotient)
            factors.add(math.pow(divisor, exponent))

            # factors.add((quotient, math.pow(divisor, exponent)))
            quotient, divisor, exponent = quotient_divisor_and_power((quotient, divisor, exponent))

        return factors


def kth_factor_2(number, k):
    """
    :param number: a positive integer
    :param k: a positive integer
    :return: the kth factor of number if there are at least k factors, -1 otherwise
    ex: kth_factor(10, 3) = 5
    """
    integers_up_to_root_of_num = generate_positive_integers_up_to_square_root_2(number)
    factors = [*map(find_factors_of_n_using_t_2, [number] * len(integers_up_to_root_of_num), integers_up_to_root_of_num)]
    unique_factors = factors[0] if len(factors) < 2 else factors[0].union(*factors[1:])
    integer_factors = [*map(int, unique_factors)]
    return -1 if k - 1 >= len(integer_factors) else sorted(integer_factors)[k - 1]

