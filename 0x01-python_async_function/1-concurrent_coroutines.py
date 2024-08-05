#!/usr/bin/env python3
""" Asynchronous coroutine """
import asyncio
import random
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ Async routine that spawn wait_random n times with
        the specified max_delay
        Args:
            n (int.): number of times to call wait_random
            max_delay (int.): maximum delay time to await
                       coroutine
        Return: list if delay time for the each coroutine
    """
    delay = await asyncio.gather(*(wait_random(max_delay)
                                 for _ in range(n)))
    return sorted(delay)
