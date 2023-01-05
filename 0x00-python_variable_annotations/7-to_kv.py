#!/usr/bin/env python3
"""
create a tuple from a string and int or float variable
"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    create a tuple

    Args:
        k (str)
        v (int or float)
    Returns:
        tuple
    """
    return (k, v)
