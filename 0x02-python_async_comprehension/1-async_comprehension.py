#!/usr/bin/env python3
"""
async comprehension
"""

import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    yield a random number between 0 and 10 while
    looping 10 times
    """
    result: List[float] = []
    async for i in async_generator():
        result.append(i)
    return(result)
