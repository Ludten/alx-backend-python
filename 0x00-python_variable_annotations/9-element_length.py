#!/usr/bin/env python3
"""
return a list of tuple with the element and its length
"""

from typing import Sequence, Iterable, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    return a list of tuple

    Args:
        lst (list)
    Returns:
        list
    """
    return [(i, len(i)) for i in lst]
