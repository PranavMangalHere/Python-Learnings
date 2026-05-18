"""
Async i/o is a Python library for writing concurrent code(structuring programs to handle multiple tasks as if they are running simultaneously)
using asyunc await syntax
i/o bound task - those tasks which are anytime waiting for something external 
Single thread is used in async it uses cooperative multitasking where tasks voluntarily give up control
for cpu bound tasks we need heavy computation so we use processes it that

Dif bitween I/o and CPU bound
"""

import asyncio
import time

def sync_function(test_param: str) -> str:
    print("This is a synchronus func")
    
    time.sleep(0.5)
    return f"Sync result: {test_param}"

# Also known as a coroutine function
async def async_func(test_param: str) -> str:
    print("This is a async coro func")
    await asyncio.sleep(0.5)
    return f"Async Result: {test_param}"

async def main():
    # sync_res = sync_function("HEllo Sync")
    # print(sync_res)
    
    # loop = asyncio.get_running_loop()
    # future = loop.create_future() # a promise like object
    # print(f"Empty Future: {future}")
    
    # future.set_result("Future Result: Test")
    # future_result = await future
    # print(f"Empty Future: {future}")
    # print(future_result)
    
    """Above CODE -  ___ IN Python their aere 3 types of awaitable objects 
    1. coroutines - creaed when you call awaitable object(anything that is written in async def is coro)
    2. Tasks - wrappers around coroutins that are scheduled on the event loop
    3. Futures - low level objects representing eventual results (-Their like promises of js but in python we don't work with 
    futures directly we use coro and and when we schedule them as tasks python uses futures under the hood to track the result-)
    """
    
    #### those functions whose execution we can pause 
    # coroutine_obj = async_func("test")
    # print(coroutine_obj)
    
    # coroutine_result = await coroutine_obj
    # print(coroutine_result)
    
    # task = asyncio.create_task(async_func("test"))
    # print(task)
    
    # task_result = await task
    # print(task_result)
    
    

if __name__ == "__main__":
    """ 
    in order to run main func we can't just call it directly
    instead we have to start an event loop 
    eventLoop - Is an engine that that runsand manages async function
    run command is starting eventloop here 
    """
    asyncio.run(main())
