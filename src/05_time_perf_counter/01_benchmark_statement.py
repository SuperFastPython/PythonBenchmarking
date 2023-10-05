# SuperFastPython.com
# example of benchmarking statement with perf_counter()
from time import perf_counter
# record start time
time_start = perf_counter()
# execute the statement
data = [i*i for i in range(100000000)]
# record end time
time_end = perf_counter()
# calculate the duration
time_duration = time_end - time_start
# report the duration
print(f'Took {time_duration:.3f} seconds')
