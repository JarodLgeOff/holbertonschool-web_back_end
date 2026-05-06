#!/usr/bin/env python3
"""Task 1: Async Comprehension"""
import asyncio
import typing

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> typing.List[float]:
    """Collect 10 random numbers using an async generator and return them"""
    return [i async for i in async_generator()]
