#!/usr/bin/env python3
""" Function for measuring runttime """
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """ Takes an integer max_delay and returns a asyncio.Task
        Args:
            max_delay (int.): maximum delay time to await
                       coroutine
        Return: asyncio.Task
    """
    return asyncio.create_task(wait_random(max_delay))
