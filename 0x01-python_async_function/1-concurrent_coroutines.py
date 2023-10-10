#!/usr/bin/env python3

import asyncio
from typing import List
from 0-basic_async_syntax import wait_random
async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn the wait_random coroutine 'n' times with specified 'max_delay'.
    Return a list of delays in ascending order.

    Args:
        n (int): The number of times to spawn the coroutine.
        max_delay (int): The maximum delay time for each coroutine.

    Returns:
        List[float]: A list of delays in ascending order.
    """
    delays = []

    tasks = [wait_random(max_delay) for _ in range(n)]

    completed_tasks = await asyncio.gather(*tasks)

    for task in completed_tasks:
        delays.append(task)

    delays.sort()

    return delays

if __name__ == "__main__":
    import random

    asyncio.run(wait_n(5, 5))
