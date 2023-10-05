# SuperFastPython.com
# example of benchmarking a statement with loop.time()
import asyncio

# define coroutine
async def main():
    # record start time
    time_start = asyncio.get_running_loop().time()
    # execute the statement
    data = [i*i for i in range(100000000)]
    # record end time
    time_end = asyncio.get_running_loop().time()
    # calculate the duration
    time_duration = time_end - time_start
    # report the duration
    print(f'Took {time_duration:.3f} seconds')

# run the coroutine
asyncio.run(main())
