import asyncio


async def fetch_data(delay, data):
    await asyncio.sleep(delay)
    print(data)


async def main():
    await asyncio.gather(
        fetch_data(1, "Data 1"),
        fetch_data(2, "Data 2"),
        fetch_data(3, "Data 3"),
    )


asyncio.run(main())
