#!/usr/bin/env python3
"""
add to all float & int variables in a list
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    sum all integers in a list

    Args:
        input_list (list)
    Returns:
        float
    """

    sum: float = 0
    for x in mxd_lst:
        sum = sum + x
    return sum
