#!/usr/bin/env python3
"""Async generator that yields random numbers with a 1 second delay"""

import asyncio
import random
import typing


async def async_generator() -> typing.Generator[float, None, None]:
    """Async generator that yields random numbers between 0 and 10 with 1 s
    delay"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
