#!/usr/bin/env python3
"""
Measure runtime
"""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measure time taken for async comprehension to
    execute
    """
    s: float = time.perf_counter()
    await async_comprehension()
    elapsed: float = time.perf_counter() - s
    return elapsed
