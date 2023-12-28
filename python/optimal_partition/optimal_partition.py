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


# def unique_substrings(word):
#     # return tz.pipe(
#     #     [[], list(word)],
#     #     ft.partial(itz.iterate, unique_substring),
#     #     ft.partial(it.dropwhile, operator.itemgetter(1)),
#     #     next,
#     #     operator.itemgetter(0)
# )


def unique_substrings(word):
    substrings, to_process = [[], list(word)]

    while to_process:
        substrings, to_process = unique_substring((substrings, to_process))

    return substrings


def optimal_partition(word):
    """
    :param word: the word to partition
    :return: the minimum number of substrings made by partitioning the word that
    contain unique characters
    """
    return len(unique_substrings(word))


def unique_substring_2(to_process):
    """
    :param to_process: the rest of the original word which
    has not been analyzed for unique substrings
    :return: what remains of the original word to analyze after finding the latest partition
    ex: unique_substring_2("aba") -> "a"
    """
    chars_consumed = set()

    rest = to_process
    while rest and rest[0] not in chars_consumed:
        current_char, *rest = rest
        chars_consumed.add(current_char)

    return rest

def optimal_partition_2(word):
    """
    :param word: the word to partition
    :return: the minimum number of substrings made by partitioning the word that
    contain unique characters
    """
    to_process = list(word)
    number_of_substrings = 0

    while to_process:
        to_process = unique_substring_2(to_process)
        number_of_substrings += 1

    return number_of_substrings

