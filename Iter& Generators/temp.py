
import threading
def cpu_task():
    count = 0
    for _ in range(10_00_000):
        count += 1
        print(count)

p1 = threading.Thread(target=cpu_task)
p2 = threading.Thread(target=cpu_task)
    
p1.start()
p2.start()

p1.join()
p2.join()


# from multiprocessing import Process

# def cpu_task():
#     count = 0
#     for _ in range(10_000_000):
#         count += 1

# p1 = Process(target=cpu_task)
# p2 = Process(target=cpu_task)

# p1.start()
# p2.start()

# p1.join()
# p2.join()


## They are giving same output becoz even the processes are running parallely but they have same CLI which means ki hamme jaise jaise process chalega waise waise waise woh apna output dega 




# import asyncio

# async def task():
#     print("Start")
#     await asyncio.sleep(2)
#     print("End")

# async def foo():
#     print("hello")
    
# async def main():
    
#     t1 = asyncio.create_task(task())
#     t2 = asyncio.create_task(foo())
    
#     await t1
#     await t2
    
# asyncio.run(main())

# import asyncio
# import time

# async def async_operation():
#     print("1️⃣ Async task started")
#     await asyncio.sleep(3)      # async I/O wait
#     print("3️⃣ Async task resumed and finished")

# async def normal_task():
#     print("2️⃣ Normal task executing")
#     time.sleep(1)               # blocking but short
#     print("2️⃣ Normal task finished")

# async def main():
#     task1 = asyncio.create_task(async_operation())
#     task2 = asyncio.create_task(normal_task())

#     await task1
#     await task2

# asyncio.run(main())
