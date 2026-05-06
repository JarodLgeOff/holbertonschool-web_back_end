#!/usr/bin/env python3
"""task 7 - To KV with annotations"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple of a string and the square of an integer/float

    Args:
        k (str): The string to be used as the key
        v (Union[int, float]): The integer or float to be squared

    Returns:
        Tuple[str, float]: A tuple of the string and the squared value as float
    """
    return (k, v ** 2)
