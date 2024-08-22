from functools import reduce
from itertools import dropwhile
from operator import add
from toolz import first, second, juxt, thread_last, iterate
from collections import namedtuple


numerals_to_integer = {"I": 1,
                       "IV": 4,
                       "V": 5,
                       "IX": 9,
                       "X": 10,
                       "XL": 40,
                       "L": 50,
                       "XC": 90,
                       "C": 100,
                       "CD": 400,
                       "D": 500,
                       "CM": 900,
                       "M": 1000}


def extract_portion_to_eval(roman_numeral: str) -> str:
    """
    :param roman_numeral: a roman numeral ranging from 1 to 3999
    :return: the largest portion of the numeral
    """
    def num_of_chars_to_extract(numeral_portion: tuple[str, str]) -> int:
        fst_part, snd_part = numeral_portion
        return 1 if numerals_to_integer[fst_part] >= numerals_to_integer[snd_part] else 2

    def extract_n_chars(num_of_chars: int) -> str:
        return roman_numeral[0: num_of_chars]

    return roman_numeral if len(roman_numeral) == 1 else thread_last(roman_numeral,
                                                                     juxt(first, second),
                                                                     num_of_chars_to_extract,
                                                                     extract_n_chars
    )


def extract_largest_portion_of_numeral(expanded_form_and_numeral: tuple[list[str], str]):
    """
    :param expanded_form_and_numeral: a collection containing the
    expanded form of a numeral and the aforementioned numeral to process
    :return: a tuple with the expanded form containing the largest portion of the
    numeral passed and the same numeral excluding what was recently extracted
    """
    def conj_string(coll, string):
        return coll + [string]

    def on_last_portion(roman_numeral):
        return extract_portion_to_eval(roman_numeral) == roman_numeral

    expanded_form, remaining_numeral = expanded_form_and_numeral
    if on_last_portion(remaining_numeral):
        return conj_string(expanded_form, remaining_numeral), []
    else:
        portion_to_eval = extract_portion_to_eval(remaining_numeral)
        return conj_string(expanded_form, portion_to_eval), remaining_numeral[len(portion_to_eval):]


def split_into_expanded_form(numeral: str) -> list[str]:
    """
    :param numeral: a roman numeral
    :return: the numeral in expanded form
    """
    def still_processing_numeral(coll):
        _, remaining_numeral = coll
        return len(remaining_numeral) != 0

    return thread_last(([], numeral),
                       (iterate, extract_largest_portion_of_numeral),
                       (dropwhile, still_processing_numeral),
                       first,
                       first)


def integer_value_of_numeral(numeral: str) -> int:
    """
    :param numeral: a roman numeral
    :return: the numerical value of the given numeral
    """
    return numerals_to_integer[numeral]


def numeral_to_integer(numeral: str) -> int:
    """
    :param numeral: a roman numeral with a value in [1, 3999]
    :return: the numerical value of the numeral
    """
    return thread_last(numeral,
                       split_into_expanded_form,
                       (map, integer_value_of_numeral),
                       (reduce, add))


def extract_portion_to_eval_2(roman_numeral: str) -> str:
    """
    :param roman_numeral: a roman numeral ranging from 1 to 3999
    :return: the largest portion of the numeral
    """
    def num_of_chars_to_extract(fst_numeral, snd_numeral) -> int:
        return 1 if numerals_to_integer[fst_numeral] >= numerals_to_integer[snd_numeral] else 2

    def extract_n_chars(num_of_chars: int) -> str:
        return roman_numeral[0: num_of_chars]

    if len(roman_numeral) == 1:
        return roman_numeral

    fst, snd = roman_numeral[0: 2]
    return extract_n_chars(num_of_chars_to_extract(fst, snd))


PartiallyEvaluatedNumeral = namedtuple("PartiallyEvaluatedNumeral",
                                       ["expanded_form", "remaining_numeral"])


def extract_largest_portion_of_numeral_2(expanded_form_and_numeral: PartiallyEvaluatedNumeral):
    """
    :param expanded_form_and_numeral: a tuple containing the
    current expanded form of a numeral and the aforementioned numeral to process
    :return: the updated expanded form of the numeral and what is left of the numeral
    to process
    """
    def conj_string(coll, string):
        return coll + [string]

    def on_last_portion(roman_numeral):
        return extract_portion_to_eval_2(roman_numeral) == roman_numeral

    expanded_form, remaining_numeral = expanded_form_and_numeral
    if on_last_portion(remaining_numeral):
        return PartiallyEvaluatedNumeral(conj_string(expanded_form,
                                                     remaining_numeral),
                                         [])
    else:
        portion_to_eval = extract_portion_to_eval_2(remaining_numeral)
        return PartiallyEvaluatedNumeral(conj_string(expanded_form, portion_to_eval),
                                         remaining_numeral[len(portion_to_eval):])


def split_into_expanded_form_2(numeral: str) -> list[str]:
    """
    :param numeral: a roman numeral
    :return: the numeral in expanded form
    """
    def iterate_until(func, pred, initial_val):
        curr_val = initial_val
        while pred(curr_val):
            curr_val = func(curr_val)

        return curr_val

    def still_expanding_numeral(expanded_form_and_numeral: PartiallyEvaluatedNumeral):
        return len(expanded_form_and_numeral.remaining_numeral) != 0

    init_val = PartiallyEvaluatedNumeral([], numeral)
    expanded_numeral, _ = iterate_until(extract_largest_portion_of_numeral_2, still_expanding_numeral, init_val)
    return expanded_numeral


def numeral_to_integer_2(numeral: str) -> int:
    """
    :param numeral: a roman numeral with a value in [1, 3999]
    :return: the numerical value of the numeral
    """
    expanded_form = split_into_expanded_form_2(numeral)
    numerical_values = map(integer_value_of_numeral, expanded_form)
    return reduce(add, numerical_values)


