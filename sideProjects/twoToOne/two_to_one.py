#!/usr/bin/env python3.6
"""
Converts two strings into a single string containing only
the characters a to z.

Usage:
    python two_to_one.py "string_one" ,"string_two"
"""
import sys


def convert_strings_to_list(str1, str2):
    """
        Converts two strings into a list object.
    :param str1:
        The first string object to convert.
    :param str2:
        The second string object to convert.
    :return:
        A list containing the two string arguments.

    >>> convert_strings_to_list("hello", "world")
    >>> ['h', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd']
    """

    converted_strings = list(str1 + str2)
    return converted_strings


def remove_illegal_characters(str_list):
    """
        Removes characters which are not allowed in the final result
        as defined by the exercise brief.
    :param str_list:
        Accepts a list object
    :return:
         Returns a new list with illegal characters removed
    """
    legal_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                     'l', ' m', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                     'v', 'w', 'x', 'y', 'z']
    legal_str_list = [letter for letter in str_list if letter in legal_letters]
    return legal_str_list


def filter_duplicates(str_list):
    """
        Takes in a list of the converted strings and returns
        a new list without duplicates.
    :param str_list:
        A list of the converted strings.
    :return:
        A list of the converted strings with duplicates removed.

    >>> filter_duplicates([ 'h', 'h', 'h', 'h', 'h','e', 'l',
     'l', 'o', 'w', 'w', 'w', 'w', 'w', 'w', 'o', 'r', 'l', 'd'])
    >>> ['h', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd']
    """
    filtered_list = list(set(str_list))
    return filtered_list


def sort_new_list(filtered_list):
    """
        Sorts the filtered list in ascending order.
    :param filtered_list:
        A list which has filtered out any duplicate items.
    :return:
        A list which has been sorted in ascending order.

    >>> sort_new_list(['o', 'd', 'r', 'l', 'w', 'e', 'h'])
    >>> ['d', 'e', 'h', 'l', 'o', 'r', 'w']
    """

    sorted_list = sorted(filtered_list)
    return sorted_list


def list_to_string(sorted_list):
    """
        Converts a sorted list back into a single string object.
    :param sorted_list:
        A list which has had any duplicates removed and sorted to be
        in alphabetical order.
    :return:
        A single string containing the sorted list elements

    >>> list_to_string(['d', 'e', 'h', 'l', 'o', 'r', 'w'])
    >>> "dehlorw"
    """
    new_str = "".join(sorted_list)
    return new_str


def convert_two_strings(str1, str2):
    list_of_string = convert_strings_to_list(str1, str2)
    list_of_string = remove_illegal_characters(list_of_string)
    list_of_string = filter_duplicates(list_of_string)
    list_of_string = sort_new_list(list_of_string)
    new_string = list_to_string(list_of_string)
    return new_string


def main(str1, str2):
    print(convert_two_strings(str1, str2))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
