#!/usr/bin/env python3
"""measure_runtime """


import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """coroutine will execute async_comprehension 4 times"""
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - start_time