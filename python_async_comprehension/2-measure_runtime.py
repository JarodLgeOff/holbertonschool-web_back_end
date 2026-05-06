#!/usr/bin/env python3
""""Task 2: Measure Runtime"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure the total runtime of async_comprehension"""
    start_time = time.time()
    coroutine = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*coroutine)
    end_time = time.time()
    return end_time - start_time
