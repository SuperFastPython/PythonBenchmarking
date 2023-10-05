# SuperFastPython.com
# example of benchmarking using a decorator
from time import perf_counter
from functools import wraps

# define the benchmark decorator
def benchmark_decorator(func):
    # inner function that wraps the target function
    @wraps(func)
    def wrapper(*args, **kwargs):
        # record start time
        time_start = perf_counter()
        # call the custom function
        result = func(*args, **kwargs)
        # record end time
        time_end = perf_counter()
        # calculate the duration
        time_duration = time_end - time_start
        # report the duration
        print(f'Took {time_duration:.3f} seconds')
        # pass on the return value
        return result
    # return the inner function
    return wrapper

# function to benchmark, with benchmark decorator
@benchmark_decorator
def task():
    # create a large list
    data = [i*i for i in range(100000000)]

# protect the entry point
if __name__ == '__main__':
    # call the custom function
    task()
