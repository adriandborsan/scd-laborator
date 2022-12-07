import asyncio
from mydelay import delay

async def main():
    task= asyncio.create_task(delay('a',10))
    try:
        result = await asyncio.wait_for(asyncio.shield(task), 5)
        print(result)
    except asyncio.TimeoutError:
        print("Please wait ...")
        result = await task
        print(result)

asyncio.run(main())
