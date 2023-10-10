#!/usr/bin/env python3

import asyncio
from typing import List
from time import perf_counter
from async_comprehension import async_comprehension  # Import the async_comprehension coroutine

async def measure_runtime() -> float:
    """
    This coroutine executes async_comprehension four times in parallel using asyncio.gather,
    measures the total runtime, and returns it.
    """
    start_time = perf_counter()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    end_time = perf_counter()
    total_runtime = end_time - start_time
    return total_runtime

async def main():
    return await measure_runtime()

if __name__ == "__main__":
    print(asyncio.run(main()))
