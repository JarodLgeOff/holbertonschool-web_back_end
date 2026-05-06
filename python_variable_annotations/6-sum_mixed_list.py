#!/usr/bin/env python3
"""Task 6 - Sum mixed list with annotations"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Returns the sum of a list of integers and floats

    Args:
        mxd_lst (List[Union[int, float]]): A list of integers and floats

    Returns:
        float: The sum of the list of integers and floats
    """
    return sum(mxd_lst)
