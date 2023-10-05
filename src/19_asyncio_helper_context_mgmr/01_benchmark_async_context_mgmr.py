# SuperFastPython.com
# example of benchmarking a coro with async context mgmr
from time import perf_counter
import asyncio

# benchmark asynchronous context manager
class Benchmark:
    # constructor
    def __init__(self, name):
        # store the name of this benchmark
        self.name = name
    # enter the async context manager
    async def __aenter__(self):
        # record the start time
        self.time_start = perf_counter()
        # return this object
        return self

    # exit the async context manager
    async def __aexit__(self, exc_type, exc, tb):
        # record the end time
        self.time_end = perf_counter()
        # calculate the duration
        self.duration = self.time_end - self.time_start
        # report the duration
        print(f'{self.name} took {self.duration:.3f} seconds')
        # do not suppress any exception
        return False

# task to benchmark
async def work():
    # create a large list
    data = [i*i for i in range(100000000)]

# main coroutine
async def main():
    # report a message
    print('Main starting')
    # benchmark the execution of our task
    async with Benchmark('work()'):
        await work()
    # report a message
    print('Main done')

# start the event loop
asyncio.run(main())
