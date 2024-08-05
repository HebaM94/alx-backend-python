#!/usr/bin/env python3
""" Asynchronous coroutine """
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ Coroutine that waits waits for a random delay 
        between 0 and max_delay seconds.
        Args:
          max_delay (int.): maximum delay time to await
                       coroutine
        Return: delay time for the coroutine
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
