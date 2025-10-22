import aiohttp
import asyncio
import time
counter = 1
async def fetch_page(url):
    global counter
    page_start = time.time()
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            counter += 1
            print(f"{counter},status code: {response.status}, time taken: {time.time()-page_start}")
            return response.status
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
# loop.run_until_complete(fetch_page("https://google.com"))
# asyncio.run(fetch_page("https://amazon.com"))
tasks = [fetch_page("https://safe-text-api-service.onrender.com/") for i in range(5)]
start = time.time()
loop.run_until_complete(asyncio.gather(*tasks))
print(f"All took {time.time()-start}")