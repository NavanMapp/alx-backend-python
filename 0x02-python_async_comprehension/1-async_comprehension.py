#!/usr/bin/env python3

import asyncio
from typing import List
from random import uniform
from async_generator import async_generator  # Import the async_generator coroutine

async def async_comprehension() -> List[float]:
    """
    This coroutine collects 10 random numbers using an async comprehension
    over the async_generator coroutine and returns the list of random numbers.
    """
    random_numbers = [number async for number in async_generator()]
    return random_numbers

async def main():
    print(await async_comprehension())

if __name__ == "__main__":
    asyncio.run(main())
