import asyncio
from mytimer import mytimer

@mytimer()
async def cpu_bound_work():
    counter = 0
    for i in range(1000000000):
        counter = counter + 1
    return counter

@mytimer()
async def main():
    task_one=asyncio.create_task(cpu_bound_work()) 
    task_two=asyncio.create_task(cpu_bound_work())
    await task_one
    await task_two

asyncio.run(main())
