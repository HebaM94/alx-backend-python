#!/usr/bin/env python3
""" Asynchronous coroutine """
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ Async routine that spawn wait_random n times with
        the specified max_delay
        Args:
            n (int.): number of times to call wait_random
            max_delay (int.): maximum delay time to await
                       coroutine
        Return: list if delay time for the each coroutine
    """
    delay = await asyncio.gather(*(task_wait_random(max_delay)
                                 for _ in range(n)))
    return sorted(delay)
