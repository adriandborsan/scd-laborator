import asyncio
from mytimer import mytimer 
from mydelay import delay


@mytimer()
async def cpu_bound_work():
    counter =0
    for i in range (100000000): 
        counter = counter + 1
    return counter

@mytimer()
async def main():
    task_one = asyncio.create_task(cpu_bound_work()) 
    task two = asyncio.create_task(cpu_bound_work()) 
    delay_task = asyncio.create_task(delay('a',4)) 
    await task_one
    await task_two 
    await delay_task

asyncio.run(main())
