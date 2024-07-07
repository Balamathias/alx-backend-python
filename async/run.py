import asyncio


wait_a_moment = __import__('main').wait_a_moment

print(asyncio.run(wait_a_moment(5)))
print(asyncio.run(wait_a_moment(10)))
print(asyncio.run(wait_a_moment(15)))

print('Hello World!')