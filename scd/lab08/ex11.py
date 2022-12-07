import asyncio
from asyncio import CancelledError
from mydelay import delay

async def main():
    print('START main ...')
    long_task = asyncio.create_task(delay('a',10))

    seconds_elapsed = 0

    while not long_task.done():
        print('Task not finished, checking again in a second.') 
        await asyncio.sleep(1)
        seconds_elapsed = seconds_elapsed + 1
        if seconds_elapsed == 5:
            long_task.cancel()
    print('.. inside main ...')
    try:
        print(' start try -')
        ---
        await long_task
        print(' end try ...')
    except CancelledError:
        print('Our task was cancelled')
        print('END main ...')

asyncio.run(main())
