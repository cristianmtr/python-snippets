import asyncio


async def main():
    print('tim')
    task = asyncio.create_task(foo('text'))
    print('finished')
    await task


async def foo(text):
    await asyncio.sleep(2)
    print(text)

if __name__ == '__main__':
    asyncio.run(main())
