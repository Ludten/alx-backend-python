#!/usr/bin/env python3
"""
Duck Typing Annotation
"""

from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')


def safely_get_value(
        dct: Mapping, key: Any, default: Union[T, None] = None
) -> Union[Any, T]:
    """
    return value of at the key in the passed dictionary

    Args:
        dct (dict)
        key (str)
        default ()
    Returns:
        any
    """
    if key in dct:
        return dct[key]
    else:
        return default
