# SuperFastPython.com
# example of benchmarking a statement with monotonic()
from time import monotonic
# record start time
time_start = monotonic()
# execute the statement
data = [i*i for i in range(100000000)]
# record end time
time_end = monotonic()
# calculate the duration
time_duration = time_end - time_start
# report the duration
print(f'Took {time_duration:.3f} seconds')
