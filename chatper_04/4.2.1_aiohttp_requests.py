import asyncio
import aiohttp
from aiohttp import ClientSession
from util import async_timed





@async_timed()
async def fetch_status(session: ClientSession, url: str) -> int:
    # задать тайм-аут
    ten_millis = aiohttp.ClientTimeout(total=.9)
    async with session.get(url, timeout=ten_millis) as result:
        return result.status

@async_timed()
async def main():
    # сессионный тайм-аут
    session_timeout = aiohttp.ClientTimeout(total=1, connect=.8)
    conn = aiohttp.TCPConnector(limit=500) # по-умолчанию, 100 одновременных соединений. 0 - значит нет ограничений


    async with aiohttp.ClientSession(timeout=session_timeout, connector=conn) as session:
        url = 'https://www.example.com'
        status = await fetch_status(session, url)
        print(f'Status for {url}\nis {status}')


asyncio.run(main())
