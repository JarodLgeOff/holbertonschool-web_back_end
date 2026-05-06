#!/usr/bin/env python3
"""Simple helper function"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Return a tuple of two integers indicating the start index and the end
    index of the indexes to be returned from a list using those specific
    pagination parameters.

    Args:
        page (int): The page number that is currently active (1-indexed).
        page_size (int): The number of elements per page.
    Returns:
        Tuple[int, int]: A tuple consisting of two integers.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
