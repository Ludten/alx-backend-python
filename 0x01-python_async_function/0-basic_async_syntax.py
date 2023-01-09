#!/usr/bin/env python3
"""
Return a random number
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Takes an integer and returns a random number
    between 0 and the integer

    Args:
        max_delay (int)

    Returns:
        float
    """
    n: float = random.uniform(0, max_delay)
    await asyncio.sleep(n)
    return n
