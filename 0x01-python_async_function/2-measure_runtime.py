#!/usr/bin/env python3

import asyncio
import time
from typing import List
from 1-concurrent_coroutines import wait_n
from 0-basic_async_syntax import wait_random
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
