# SuperFastPython.com
# example of benchmarking a coroutine with a decorator
from time import perf_counter
from functools import wraps
import asyncio

# define the benchmark decorator
def benchmark(coro):
    # inner coroutine that wraps the target coro
    @wraps(coro)
    async def wrapped(*args, **kwargs):
        # record start time
        time_start = perf_counter()
        try:
            # await the target
            return await coro(*args, **kwargs)
        finally:
            # record end time
            time_end = perf_counter()
            # calculate the duration
            time_duration = time_end - time_start
            # report the duration
            name = coro.__name__
            print(f'{name} Took {time_duration:.3f} s')
    # return the wrapped coro
    return wrapped

# work to benchmark
@benchmark
async def work():
    # create a large list
    data = [i*i for i in range(100000000)]

# main coroutine
async def main():
    # report a message
    print('Main starting')
    # benchmark the execution of our task
    await work()
    # report a message
    print('Main done')

# start the event loop
asyncio.run(main())
