#!/usr/bin/env python3

import asyncio

from 0-basic_async_syntax import wait_random

def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create an asyncio.Task from the wait_random coroutine with the specified max_delay.

    Args:
        max_delay (int): Maximum delay in seconds for wait_random.

    Returns:
        asyncio.Task: A task representing the execution of wait_random.
    """
    return asyncio.ensure_future(wait_random(max_delay))

if __name__ == "__main__":
    async def test(max_delay: int) -> float:
        task = task_wait_random(max_delay)
        await task
        print(task.__class__)

    asyncio.run(test(5))
