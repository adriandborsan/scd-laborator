from asyncio import Future 
import asyncio
from mydelay import delay

async def set_future_value(fval): 
    await asyncio.sleep(3)
    fval.set_result(42)

def make_request():
    f = Future()
    asyncio.create_task(set_future_value(f))
    return f

async def main():
    future make_request()
    print(f'Done: {future.done()}")
    value = await future
    print(f'Done: {future.done()}") 
    print(f'Value: {value}")

asyncio.run(main())
