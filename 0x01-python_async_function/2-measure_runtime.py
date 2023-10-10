#!/usr/bin/env python3

import asyncio
import time
from typing import List
import random
async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random
    delay between 0 and max_delay seconds
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
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
def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time for wait_n(n, max_delay)
    and return the average time per call.

    Args:
        n (int): Number of times to call wait_n.
        max_delay (int): Maximum delay in seconds for each wait_n call.

    Returns:
        float: Average time per call in seconds.
    """
    start_time = time.time()

    loop = asyncio.get_event_loop()

    delays = loop.run_until_complete(wait_n(n, max_delay))

    end_time = time.time()
    total_time = end_time - start_time

    average_time = total_time / n

    return average_time
if __name__ == "__main__":
    n = 5
    max_delay = 9
    print(measure_time(n, max_delay))
