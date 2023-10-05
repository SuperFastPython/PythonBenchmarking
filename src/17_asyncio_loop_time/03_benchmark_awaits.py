# SuperFastPython.com
# example of benchmarking a coroutine that awaits
import asyncio

# our work coroutine
async def work():
    # sleep a moment
    await asyncio.sleep(1)

# define coroutine
async def main():
    # record start time
    time_start = asyncio.get_running_loop().time()
    # await the target coroutine
    await work()
    # record end time
    time_end = asyncio.get_running_loop().time()
    # calculate the duration
    time_duration = time_end - time_start
    # report the duration
    print(f'Took {time_duration:.3f} seconds')

# run the coroutine
asyncio.run(main())
