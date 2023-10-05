# SuperFastPython.com
# example of a benchmark context manager
from time import perf_counter

# define the benchmark context manager
class Benchmark:
    # constructor
    def __init__(self, name):
        # store the name of this benchmark
        self.name = name

    # enter the context manager
    def __enter__(self):
        # record the start time
        self.time_start = perf_counter()
        # return this object
        return self

    # exit the context manager
    def __exit__(self, exc_type, exc_value, traceback):
        # record the end time
        self.time_end = perf_counter()
        # calculate the duration
        self.duration = self.time_end - self.time_start
        # report the duration
        print(f'{self.name} took {self.duration:.3f} s')
        # do not suppress any exception
        return False

# function to benchmark
def task():
    # create a large list
    data = [i*i for i in range(100000000)]

# protect the entry point
if __name__ == '__main__':
    # create the benchmark context
    with Benchmark('Task'):
        # run the task
        task()
