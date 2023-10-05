# SuperFastPython.com
# example of benchmarking a coroutine
import asyncio

# our work coroutine
async def work():
    # do some CPU bound work
    data = [i*i for i in range(100000000)]

# define coroutine
async def main():
    # record start time
    time_start = asyncio.get_running_loop().time()
    # suspend and await the coroutine
    await work()
    # record end time
    time_end = asyncio.get_running_loop().time()
    # calculate the duration
    time_duration = time_end - time_start
    # report the duration
    print(f'Took {time_duration:.3f} seconds')

# run the coroutine
asyncio.run(main())
