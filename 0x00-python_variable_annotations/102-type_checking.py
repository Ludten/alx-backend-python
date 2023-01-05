#!/usr/bin/env python3
"""
mypy Typing Annotation
"""

from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    multiply elements in tuple by factor

    Args:
        lst (tuple)
        factor (int)
    Returns:
        List
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
