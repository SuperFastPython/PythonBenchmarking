# SuperFastPython.com
# example of benchmarking a function with thread_time()
from time import thread_time

# function to benchmark
def task():
    # create a large list
    data = [i*i for i in range(100000000)]

# record start time
time_start = thread_time()
# execute the function
task()
# record end time
time_end = thread_time()
# calculate the duration
time_duration = time_end - time_start
# report the duration
print(f'Took {time_duration:.3f} seconds')
