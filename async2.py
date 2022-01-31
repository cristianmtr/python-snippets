import asyncio


async def fetch_data():
    print(f'starting')
    await asyncio.sleep(1)
    print(f'got data')
    return {'data': 1}


async def print_numbers():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.5)


async def main():
    task1 = asyncio.create_task(fetch_data())
    task2 = asyncio.create_task(print_numbers())

    await task1
    await task2

if __name__ == '__main__':
    asyncio.run(main())
