import asyncio
from mydelay import delay

async def add_one(number): 
    return number + 1

async def hello_world_message(): 
    await delay('a', 1)
    return 'Hello World!'

async def main():
    message = await hello_world_message()
    one_plus_one = await add_one(1)
    print(one_plus_one)
    print(message)

asyncio.run(main())
