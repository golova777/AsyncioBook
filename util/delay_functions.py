import asyncio
from util.decorators import async_timed


@async_timed()
async def delay(seconds: int) -> int:
    print(f"Засыпаю на {seconds} секунд")
    await asyncio.sleep(seconds)
    print(f"Сон в течение {seconds} секунд закончился.")
    return seconds
