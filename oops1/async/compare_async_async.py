import aiohttp
import asyncio
import time

urls = [
    "https://httpbin.org/delay/1",
    "https://httpbin.org/delay/2",
    "https://httpbin.org/delay/3",
]


async def fetch_url(session, url):
    async with session.get(url) as response:
        return await response.text()


async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
        for url, result in zip(urls, results):
            print(f"Fetched data from {url}")


start_time = time.time()

asyncio.run(main())

end_time = time.time()
print(f"Total time taken: {end_time - start_time} seconds")
