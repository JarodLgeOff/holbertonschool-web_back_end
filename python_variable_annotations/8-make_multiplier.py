#!/usr/bin/env python3
"""Task 8 - Make multiplier with annotations"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a float by multiplier

    Args:
        multiplier (float): The multiplier to multiply the float by

    Returns:
        Callable[[float], float]: A function that multiplies a float by
          multiplier
    """
    def multiplier_func(x: float) -> float:
        """Multiplies a float by multiplier

        Args:
            x (float): The float to multiply by multiplier

        Returns:
            float: The result of multiplying x by multiplier
        """
        return x * multiplier
    return multiplier_func
