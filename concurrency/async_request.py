import aiohttp
import asyncio

async def fetch_page(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print(response.status)
            return response.status
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
loop.run_until_complete(fetch_page("https://google.com"))
asyncio.run(fetch_page("https://amazon.com"))