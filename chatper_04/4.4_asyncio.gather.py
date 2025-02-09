import asyncio
import aiohttp
from aiohttp import ClientSession
from chatper_04 import fetch_status
from util import async_timed


@async_timed()
async def main():
    session_timeout = aiohttp.ClientTimeout(total=3, connect=.5)
    async with ClientSession(timeout=session_timeout) as session:
        urls = ['https://www.example.com/' for _ in range(10)]
        # в requests попадут 1000 корутин
        requests = [fetch_status(session, url) for url in urls]
        # а теперь выполним конкурентно все задачи/корутины
        status_codes = await asyncio.gather(*requests)
        print(status_codes)


asyncio.run(main())

# далее 4.4.1 обработка исключений при использовании gather
