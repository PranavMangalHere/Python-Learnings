import asyncio
import time

## One of the most correct way to get concurrency

async def fetch_data(param):
    print(f"Do something with {param}...")
    await asyncio.sleep(param)
    print(f"Done with {param}")
    return f"Result of {param}"


async def main():
    task1 = asyncio.create_task(fetch_data(1))
    task2 = asyncio.create_task(fetch_data(2))
    result2 = await task2
    print("Task 2 fully completed")
    result1 = await task1
    print("Task 1 fully completed")
    return [result1, result2]

t1 = time.perf_counter()
result = asyncio.run(main())
print(result)

t2 = time.perf_counter()

print(f"Finished in {t2 - t1:.2f} seconds")
