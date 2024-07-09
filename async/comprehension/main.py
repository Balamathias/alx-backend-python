'''Trying async comprehension'''

import asyncio
from typing import Any, AsyncGenerator

async def numbers(start: int = 0, end: int = 20) -> AsyncGenerator[int, Any]:
    for i in range(start, end):
        yield i
        await asyncio.sleep(1)

    
async def main():
    async for i in numbers(end=50):
        print(i)


if __name__ == '__main__':
    asyncio.run(main())
