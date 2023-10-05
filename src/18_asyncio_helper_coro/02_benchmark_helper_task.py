# SuperFastPython.com
# example of benchmarking a task with a helper coroutine
from time import perf_counter
import asyncio

# benchmark coroutine
async def benchmark(awaitable):
    # record start time
    time_start = perf_counter()
    try:
        # await the target
        await awaitable
    finally:
        # record end time
        time_end = perf_counter()
        # calculate the duration
        time_duration = time_end - time_start
        # report the duration
        print(f'Took {time_duration:.3f} seconds')

# task to benchmark
async def work():
    # create a large list
    data = [i*i for i in range(100000000)]

# main coroutine
async def main():
    # report a message
    print('Main starting')
    # create the task
    task = asyncio.create_task(work())
    # benchmark the execution of our task
    await benchmark(task)
    # report a message
    print('Main done')

# start the event loop
asyncio.run(main())
