#!/usr/bin/env python3
"""
Duck Typing Annotation
"""

from typing import Sequence, Union, Any

# The types of the elements of the input are not know


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    return first element of list is not none

    Args:
        lst (list)
    Returns:
        any
    """
    if lst:
        return lst[0]
    else:
        return None
