#!/usr/bin/env python3
"""
Return a list of floats
"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Takes two integers and returns a list of floats
    between 0 and the integer

    Args:
        int (int)
        max_delay (int)

    Returns:
        List[float]
    """
    delaylist = await asyncio.gather(*(task_wait_random(max_delay)
                                       for i in range(n)))
    return sorted(delaylist)
