
"""Measure runtime"""
import asyncio
import time
from typing import List
async_comprehension = __import__('1-async_comprehension').async_generator


async def measure_runtime() -> float:
    """
    measure_runtime - function to measure the runtime
    Arguments:
        no arguments
    Returns:
        float: the time taken to execute the function
    """
    start = time.time()
    await asyncio.gather(*([async_comprehension() for i in range(4)]))
    end = time.time()
    print( end - start)


if __name__ == "__main__":
    asyncio.run(measure_runtime())