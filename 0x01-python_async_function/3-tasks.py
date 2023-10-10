#!/usr/bin/env python3

import asyncio
import random
async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random
    delay between 0 and max_delay seconds
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
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
