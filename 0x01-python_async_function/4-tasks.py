#!/usr/bin/env python3

import asyncio
from typing import List

from 3-tasks import task_wait_random

async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Create an asyncio.Task for wait_random n times with the specified
    max_delay and return the sorted list of delays.

    Args:
        n (int): Number of times to call task_wait_random.
        max_delay (int): Maximum delay in seconds
        for each task_wait_random call.

    Returns:
        List[float]: List of delays in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    await asyncio.gather(*tasks)
    delays = [task.result() for task in tasks]
    return sorted(delays)

if __name__ == "__main__":
    n = 5
    max_delay = 6
    print(asyncio.run(task_wait_n(n, max_delay)))
