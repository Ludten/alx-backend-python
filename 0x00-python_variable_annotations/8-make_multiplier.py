#!/usr/bin/env python3
"""
return a function that multiplies a float
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    pass the multiplier to a function and return
    the function

    Args:
        multiplier (float)
    Returns:
        function
    """

    def mul(a: float) -> float:
        """
        multiple pass multiplier and new value

        Args:
            a (float)
        Returns:
            float
        """
        return multiplier * a

    return mul
