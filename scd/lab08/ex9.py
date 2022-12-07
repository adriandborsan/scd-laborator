import asyncio
from mydelay import delay
from datetime import datetime

start time=datetime.now()

async def main():
    print('START main ...')
    sleep_a = asyncio.create_task(delay('a',3))
    sleep_b = asyncio.create_task(delay('b',5))
    sleep_c = asyncio.create_task(delay('c',2))
   
    await sleep_a
    await sleep_b
    await sleep_c
    print('END main ...')

asyncio.run(main())

print("Duration: {}'.format(datetime.now()-start_time))
