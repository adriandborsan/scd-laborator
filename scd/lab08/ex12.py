import asyncio
from mydelay import delay

async def main():
    print('START main ...')
    delay_task = asyncio.create_task(delay('a',5))
    try:
        print("... start try ...')
        result = await asyncio.wait_for(delay_task, timeout=2) 
        print(result)
        print('... end try ...')
    except asyncio.exceptions.TimeoutError:
        print(f'task is cancelled: {delay_task.cancelled()}')
        print('END main ...')

asyncio.run(main())
