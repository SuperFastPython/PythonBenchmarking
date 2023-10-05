# SuperFastPython.com
# example of benchmarking using a custom function
from time import perf_counter

# benchmark function
def benchmark(fun, *args):
    # record start time
    time_start = perf_counter()
    # call the custom function
    fun(*args)
    # record end time
    time_end = perf_counter()
    # calculate the duration
    time_duration = time_end - time_start
    # report the duration
    print(f'Took {time_duration:.3f} seconds')

# function to benchmark
def task():
    # create a large list
    data = [i*i for i in range(100000000)]

# protect the entry point
if __name__ == '__main__':
    # benchmark the task() function
    benchmark(task)
