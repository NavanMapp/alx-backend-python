#!/usr/bin/env python3

import asyncio
from typing import List
from random import uniform
async_generator = __import__('0-async_generator').async_generator
async def async_comprehension() -> List[float]:
    """
    This coroutine collects 10 random numbers using an async comprehension
    over the async_generator coroutine and returns the list of random numbers.
    """
    return [num async for num in async_generator()][:10]
async def main():
    print(await async_comprehension())
