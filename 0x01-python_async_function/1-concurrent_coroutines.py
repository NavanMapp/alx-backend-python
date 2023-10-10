#!/usr/bin/env python3

import asyncio
from typing import List

# Import the wait_random coroutine from the previous file
from 0-basic_async_syntax import wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous coroutine that spawns wait_random n times with the specified max_delay.

    Args:
        n (int): Number of times to call wait_random.
        max_delay (int): Maximum delay in seconds for each wait_random call.

    Returns:
        List[float]: List of delays in ascending order.
    """
    delays = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    return sorted(delays)

if __name__ == "__main__":
    # Test cases
    print(asyncio.run(wait_n(5, 5)))
    print(asyncio.run(wait_n(10, 7)))
    print(asyncio.run(wait_n(10, 0)))
