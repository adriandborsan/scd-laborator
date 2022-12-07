import asyncio
from mydelay import delay 
from datetime import datetime

start_time = datetime.now()

async def hello_every_second(): 
    for i in range(4):
        await asyncio.sleep(1)
        print("I'm running other code while I'm waiting!")

async def main():
    print('START main ... ..')
    delay_a = asyncio.create_task(delay('a',5)) 
    delay_b = asyncio.create_task(delay('b',3)) 
    await hello_every_second()
    await delay_a
    await delay_b
    print('END main ...')

asyncio.run(main())
print('Duration: {}'.format(datetime.now()-start_time))
