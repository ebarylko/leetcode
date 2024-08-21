from functools import reduce
from itertools import dropwhile
from toolz import concat, first, second, juxt, thread_last, iterate, take


numerals_to_integer = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


def extract_portion_to_eval(roman_numeral: str) -> str:
    """
    :param roman_numeral: a roman numeral ranging from 1 to 3999
    :return: the largest unit of the numeral
    """
    def num_of_chars_to_extract(numeral_portion: tuple[str, str]) -> int:
        fst_part, snd_part = numeral_portion
        return 1 if numerals_to_integer[fst_part] >= numerals_to_integer[snd_part] else 2

    def extract_n_chars(num_of_chars: int) -> str:
        return roman_numeral[0: num_of_chars]

    return thread_last(roman_numeral,
                       juxt(first, second),
                       num_of_chars_to_extract,
                       extract_n_chars
    )


def split_into_expanded_form(numeral: str) -> list[str]:
    """
    :param numeral: a roman numeral
    :return: the portions of the given numeral to evaluate
    when determining the numerical value
    """
    def on_last_portion(roman_numeral):
        return extract_portion_to_eval(roman_numeral) == roman_numeral

    def add_portion_of_numeral_to_eval(remaining_numeral_and_portions_to_eval: tuple[list[str], str]):
        expanded_form, remaining_numeral = remaining_numeral_and_portions_to_eval
        if on_last_portion(numeral):
            return expanded_form + [remaining_numeral], []
        else:
            portion_to_eval = extract_portion_to_eval(remaining_numeral)
            return expanded_form + [portion_to_eval], remaining_numeral[len(portion_to_eval):]

    def still_processing_numeral(coll):
        _, remaining_numeral = coll
        return len(remaining_numeral) != 0

    return thread_last(([], numeral),
                       (iterate, add_portion_of_numeral_to_eval),
                       (dropwhile, still_processing_numeral),
                       first,
                       first)


def numeral_to_integer(numeral: str) -> int:
    """
    :param numeral:
    :return:
    """
    return 8

