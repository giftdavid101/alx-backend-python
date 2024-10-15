#!/usr/bin/env python3
'''Async Generator'''


import asyncio
import random
import typing



async def async_generator() -> typing.Generator[float, None, None]:
    """Loop 10 times """

    for i in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
