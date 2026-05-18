import asyncio
import time

async def fetch_data(param):
    print(f"Do Somehing with {param}....")
    await asyncio.sleep(param)
    print("Done with {param}")
    return f"Result of {param}"

async def main():
    task1 = fetch_data(1) # could be awaited directly
    task2 = fetch_data(2)
    result1 = await task1
    print("Task 1 fully completed")
    result2 = await task2
    print("Task 2 fully completed")
    return [result1, result2]

t1 = time.perf_counter()

results = asyncio.run(main())
print(results)

t2 = time.perf_counter()
print(f"Finished in {t2 - t1:.2f} seconds")


"""
Output --- 
Do Somehing with 1....
Done with {param}
Task 1 fully completed
Do Somehing with 2....
Done with {param}
Task 2 fully completed
['Result of 1', 'Result of 2']
  ---->>Finished in 3.01 seconds__
"""

""" even if we make fuctions async we havn't got the concurrency benifit here  """