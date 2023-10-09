#!/usr/bin/env python3
"""
Take the code from wait_n and alter it into a new function task_wait_n.
The code is nearly identical to wait_n except
task_wait_random is being called.
"""
import asyncio
from typing import List
from 3-tasks import task_wait_random
async def task_wait_n(n: int, max_delay: int) -> List[float]:
    results = []
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*tasks)
    results.sort()
    return results
