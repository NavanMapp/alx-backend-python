#!/usr/bin/env python3
"""
Write a function (do not create an async function, use the regular function
syntax to do this) task_wait_random that takes an integer max_delay and returns
a asyncio.Task
"""
import asyncio
from typing import Coroutine
from 0-basic_async_syntax import wait_random
def task_wait_random(max_delay: int) -> asyncio.Task:
    coroutine = wait_random(max_delay)
    loop = asyncio.get_event_loop()
    task = loop.create_task(coroutine)
    return task
