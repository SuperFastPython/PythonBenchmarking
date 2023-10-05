# SuperFastPython.com
# example a variability in benchmark results
from time import perf_counter

# function to benchmark
def task():
    # create a large list
    data = [i*i for i in range(100000000)]

# benchmark the task() function
def benchmark():
    # record start time
    time_start = perf_counter()
    # execute the function
    task()
    # record end time
    time_end = perf_counter()
    # calculate the duration
    time_duration = time_end - time_start
    # report the duration
    print(f'Took {time_duration:.3f} seconds')

# repeat the same benchmark a few times
benchmark()
benchmark()
benchmark()
