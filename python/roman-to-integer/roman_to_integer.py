from functools import reduce
from toolz import concat, first, second, juxt


numerals_to_integer = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


def extract_portion_to_eval(roman_numeral: str) -> str:
    """
    :param roman_numeral: a roman numeral ranging from 1 to 3999
    :return: the largest unit of the numeral
    """
    def first_and_second(coll):
        return juxt(first, second)(coll)

    def num_of_chars_to_extract(numeral_1: str, numeral_2: str) -> int:
        return 1 if numerals_to_integer[numeral_1] >= numerals_to_integer[numeral_2] else 2

    first_char, second_char = first_and_second(roman_numeral)
    return roman_numeral[0: num_of_chars_to_extract(first_char, second_char)]


# def split_into_expanded_form(numeral: str) -> list[str]:
#     """
#     :param numeral: a roman numeral
#     :return: the portions of the given numeral to evaluate
#     when determining the numerical value
#     """
#     def add_portion_of_numeral_to_eval(to_evaluate: list[str], remaining_numeral: str):
#         if len(str) == 1:
#             return concat([to_evaluate, remaining_numeral])
#
#         portion = extract_portion(remaining_numeral)
#
#     return reduce()

def numeral_to_integer(numeral: str) -> int:
    """
    :param numeral:
    :return:
    """
    return 8

