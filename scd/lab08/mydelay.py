import asyncio

async def delay (who, delay_seconds):
    print(f'{who} will sleep for {delay_seconds} second(s)')
    await asyncio.sleep(delay_seconds)
    print(f'{who} finished sleeping for {delay_seconds} second(s)')
    return delay_seconds
    