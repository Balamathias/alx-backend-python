#!/bin/usr/env python3

'''My first async generator comprehension in Python'''

import asyncio
import random
from typing import Any, AsyncGenerator


async def async_generator() -> AsyncGenerator[float, Any]:
    '''Async generator that yields random numbers'''
    for _ in range(10):
        await asyncio.sleep(1)
        yield (random.random() * 10)
