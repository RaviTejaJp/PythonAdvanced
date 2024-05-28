import asyncio


async def fetch_data(delay, data):
    await asyncio.sleep(delay)
    print(data)


async def main():
    task1 = asyncio.create_task(fetch_data(1, "Data 1"))
    task2 = asyncio.create_task(fetch_data(2, "Data 2"))
    task3 = asyncio.create_task(fetch_data(3, "Data 3"))

    await task1
    await task2
    await task3


asyncio.run(main())
