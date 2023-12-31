#!/usr/bin/env python3

import time
from typing import Callable

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
    wait_n(n, max_delay)
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
if __name__ == "__main__":
    n = 5
    max_delay = 9
    print(measure_time(n, max_delay))
