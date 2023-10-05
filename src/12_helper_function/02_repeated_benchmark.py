# SuperFastPython.com
# example of benchmarking using a custom function
from time import perf_counter

# repeated benchmark function
def repeated_benchmark(fun, n_repeats, *args):
    results = list()
    # repeat the benchmark many times
    for i in range(n_repeats):
        # record start time
        time_start = perf_counter()
        # call the custom function
        fun(*args)
        # record end time
        time_end = perf_counter()
        # calculate the duration
        time_duration = time_end - time_start
        # store the result
        results.append(time_duration)
        # report progress
        print(f'>{i+1} took {time_duration:.3f} sec')
    # calculate average duration
    avg_duration = sum(results) / n_repeats
    # report the average duration
    print(f'Took {avg_duration:.3f} sec on average')

# function to benchmark
def task():
    # create a large list
    data = [i*i for i in range(100000000)]

# protect the entry point
if __name__ == '__main__':
    # benchmark the task() function
    repeated_benchmark(task, 3)
