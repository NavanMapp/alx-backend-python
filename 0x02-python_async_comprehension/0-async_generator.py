#!/usr/bin/env python3

import asyncio
import random
async def async_generator():
    """
    This coroutine generates random numbers between 0 and 10 asynchronously,
    with a 1-second delay between each yield.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
async def print_yielded_values():
    result = []
    async for i in async_generator():
        result.append(i)
    print(result)
if __name__ == "__main__":
    asyncio.run(print_yielded_values())