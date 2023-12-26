import functools as ft
import operator

import toolz as tz
import toolz.itertoolz as itz
import itertools as it


def unique_substring(tuple):
    """
    :param substrings: a collection of the unique substrings
    :param to_process: the rest of the original word which
    has not been analyzed for unique substrings
    :return: the collection of unique substrings with the newest
    unique substring found in to_process
    """
    substrings, to_process = tuple
    chars_consumed = set()

    rest = to_process
    substring = ""
    while rest and rest[0] not in chars_consumed:
        current_char, *rest = rest
        chars_consumed.add(current_char)
        substring += current_char

    substrings.append(substring)

    return substrings, rest


def unique_substrings(word):
    return tz.pipe(
        [[], list(word)],
        ft.partial(itz.iterate, unique_substring),
        ft.partial(it.dropwhile, operator.itemgetter(1)),
        next,
        operator.itemgetter(0)
        # list
    )


def optimal_partition(word):
    """
    :param word: the word to partition
    :return: the minimum number of substrings made by partitioning the word that
    contain unique characters
    """
    return unique_substrings(word)