#!/usr/bin/env python3
"""
Return the runtime of function
"""

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Takes two integers and returns the time it takes
    for the function to execute

    Args:
        int (int)
        max_delay (int)

    Returns:
        float
    """
    s: float = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed: float = time.perf_counter() - s
    return elapsed
