import asyncio
from mydelay import delay 
from datetime import datetime

start_time = datetime.now()

async def main():
    print('START main ...')
    sleep_a
    =
    asyncio.create_task(delay('a',3))
    print(type(sleep_a))
    result = await sleep_a
    print(result)
    print('END main .")

asyncio.run(main())

print('Duration: {}'.format(datetime.now() start_time))
