#!/usr/bin/env python3
"""
Concurrent Coroutines
"""

import asyncio
from typing import List
from 0-basic_async_syntax import wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    results = []
    tasks = [wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*tasks)
    results.sort()
    return results