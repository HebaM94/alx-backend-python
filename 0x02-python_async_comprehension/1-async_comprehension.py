#!/usr/bin/env python3
""" Asynchronous coroutine """
import asyncio
import random
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ Coroutine that collect 10 random numbers using an async
        comprehensing over async_generator
        Args:
          None
        Return: The 10 random numbers.
    """
    return [i async for i in async_generator()]
