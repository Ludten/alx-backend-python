#!/usr/bin/env python3
"""
add to all float numbers in a list of floats
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    sum all float in a list of floats

    Args:
        input_list (list)
    Returns:
        float
    """

    sum: float = 0
    for x in input_list:
        sum = sum + x
    return sum
