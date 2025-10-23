import aiohttp
import asyncio
import async_timeout
import time
counter = 1

# async def get_session():
#     async with aiohttp.ClientSession() as session:
#         return session
async def get_multiple_pages(loop,*urls):
    tasks = []
    async with aiohttp.ClientSession(loop=loop) as session:
        for url in urls:
            tasks.append(fetch_page(session,url))
        grouped_tasks = asyncio.gather(*tasks)
        return await grouped_tasks

async def fetch_page(session,url):
    global counter
    page_start = time.time()
    async with async_timeout.timeout(500):
        async with session.get(url) as response:
            counter += 1
            print(f"{counter},status code: {response.status}, time taken: {time.time()-page_start}")
            return response.status
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
# loop.run_until_complete(fetch_page("https://google.com"))
# asyncio.run(fetch_page("https://amazon.com"))
urls = ["https://safe-text-api-service.onrender.com/" for i in range(500)]
start = time.time()
loop.run_until_complete(get_multiple_pages(loop,*urls))
print(f"All took {time.time()-start}")