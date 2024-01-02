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
        list
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
        (tz.mapcat, find_factors_for_each_value),
        set,
        lambda coll: -1 if k >= len(coll) else coll[k]
        # math.sqrt,
        # math.floor,
        # (op.add, 1),
        # range,
        # list,

    )
