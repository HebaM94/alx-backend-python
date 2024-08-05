#!/usr/bin/env python3
""" Function for measuring runttime """
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ Measures the total execution time for
        wait_n(n, max_delay)
        Args:
            n (int.): number of times to call wait_random
            max_delay (int.): maximum delay time to await
                       coroutine
        Return: total_time / n
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    return (end_time - start_time)/n
