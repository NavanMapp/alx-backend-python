#!/usr/bin/env python3

import asyncio
import time

from 1-concurrent_coroutines import wait_n
def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay)
    and returns the average time per execution.

    Args:
        n (int): Number of times to call wait_n.
        max_delay (int): Maximum delay in seconds for each wait_n call.

    Returns:
        float: Average time per execution in seconds.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
if __name__ == "__main__":
    n = 5
    max_delay = 9
    print(measure_time(n, max_delay))
