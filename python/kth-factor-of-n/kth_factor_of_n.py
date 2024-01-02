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
    def divide_by(divide, num):
        return op.truediv(num, divide)

    return {1, number} if divisor == 1 or number % divisor != 0 else tz.thread_last(
        (number, divisor, 0),
        (tz.iterate, quotient_divisor_and_power),
        (it.takewhile, lambda t: t[0] - int(t[0]) == 0),
        (map, tz.juxt(tz.compose(int, tz.first), tz.compose(int, tz.partial(math.pow, divisor), tz.last))),
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
        (tz.map, tz.partial(find_factors_of_n_using_t, number)),
        list
        # set,
        # lambda coll: -1 if k >= len(coll) else coll[k]

    )
