import asyncio
import random
from time import sleep
from typing import Union


async def wait_a_moment(duration: Union[int, float]) -> Union[int, float]:
    delay = random.uniform(0, duration)
    await asyncio.sleep(delay)
    return delay
