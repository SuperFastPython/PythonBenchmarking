# SuperFastPython.com
# example a stable benchmark results
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
    # return the duration
    return time_duration

# repeat a benchmark
def repeat_benchmark():
    # define the number of repeats
    n_repeats = 30
    # list for storing all results
    all_times = list()
    # repeat benchmark may times
    for i in range(n_repeats):
        # benchmark and retrieve the duration
        time_duration = benchmark()
        # report the duration
        print(f'>{i} took {time_duration:.3f} seconds')
        # store the result
        all_times.append(time_duration)
    # calculate the average duration
    time_avg = sum(all_times) / n_repeats
    # report the average time
    print(f'Took {time_avg:.3f} seconds on average')

# execute a repeated benchmark
repeat_benchmark()
