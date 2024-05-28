import aiohttp
import asyncio


async def fetch_url(session, url):
    async with session.get(url) as response:
        return await response.text()


async def main(url):
    async with aiohttp.ClientSession() as session:
        html = await fetch_url(session, url)
        print(html)


asyncio.run(main(url="https://www.google.com"))
asyncio.run(main(url="https://www.youtube.com"))
