#!/usr/bin/env python3
"""
Measure Runtime
"""

import asyncio
import time
from typing import List
from 1-concurrent_coroutines import wait_n

def measure_time(n: int, max_delay: int) -> float:
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    average_time = total_time / n
    return average_time