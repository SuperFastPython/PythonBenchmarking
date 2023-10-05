# SuperFastPython.com
# example of benchmarking average time using a decorator
from time import perf_counter
from functools import wraps

# define the average benchmark decorator
def average_benchmark_decorator(func):
    # inner function that wraps the target function
    @wraps(func)
    def wrapper(*args, **kwargs):
        results = list()
        # repeat the benchmark many times
        n_repeats = 3
        for i in range(n_repeats):
            # record start time
            time_start = perf_counter()
            # call the custom function
            result = func(*args, **kwargs)
            # record end time
            time_end = perf_counter()
            # calculate the duration
            time_duration = time_end - time_start
            # store the result
            results.append(time_duration)
            # report progress
            print(f'>{i+1} took {time_duration:.3f} s')
        # calculate average duration
        avg_duration = sum(results) / n_repeats
        # report the average duration
        print(f'Took {avg_duration:.3f} sec on average')
        # pass on the return value
        return result
    # return the inner function
    return wrapper

# function to benchmark, with benchmark decorator
@average_benchmark_decorator
def task():
    # create a large list
    data = [i*i for i in range(100000000)]

# protect the entry point
if __name__ == '__main__':
    # call the custom function
    task()
