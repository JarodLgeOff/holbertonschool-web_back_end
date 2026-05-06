#!/usr/bin/env python3
"""Task 1: Concatenate two strings with annotations."""


def concat(str1: str, str2: str) -> str:
    """Returns the concatenation of str1 and str2 as a string.

    Args:
        str1 (str): The first string to concatenate.
        str2 (str): The second string to concatenate.

    Returns:
        str: The concatenation of str1 and str2.
    """
    return "{}{}".format(str1, str2)
