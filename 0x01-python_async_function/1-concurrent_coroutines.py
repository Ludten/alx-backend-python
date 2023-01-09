#!/usr/bin/env python3
"""
Return a list of floats
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Takes two integers and returns a list of floats
    between 0 and the integer

    Args:
        int (int)
        max_delay (int)

    Returns:
        List[float]
    """
    delaylist = await asyncio.gather(*(wait_random(max_delay)
                                       for i in range(n)))
    return sorted(delaylist)
