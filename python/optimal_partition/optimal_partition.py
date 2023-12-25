import functools as ftz
import toolz.itertoolz as itz

def unique_substring(substrings, to_process):
    """
    :param substrings: a collection of the unique substrings
    :param to_process: the rest of the original word which
    has not been analyzed for unique substrings
    :return: the collection of unique substrings with the newest
    unique substring found in to_process
    """
    chars_consumed = set()

    current_char, rest = [itz.first(to_process), itz.drop(1, to_process)]
    # return [current_char, list(rest)]
    substring = ""
    while current_char and current_char not in chars_consumed:
        chars_consumed.add(current_char)
        substring += str(current_char)
        rest = list(itz.drop(1, to_process))
        current_char = list(itz.take(1, rest))
    substrings.append(substring)
    return [substrings, rest]



def unique_substrings(word):
    return reduce(unique_substring, word, [])

def optimal_partition(word):
    """
    :param word: the word to partition
    :return: the minimum number of substrings made by partitioning the word that
    contain unique characters
    """
    return unique_substrings(word)