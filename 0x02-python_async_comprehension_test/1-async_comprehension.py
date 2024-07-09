
""" a python module to loop 10 times """
import random
import asyncio

async_generator = __import__('0-async_generator').async_generator

async def  async_comprehension() -> list[float]:
    """
    async_comprehension - function to loop 10 times
    Arguments:
        no arguments
    Returns:
        nothing
    """
    return [i async for i in async_generator()]
