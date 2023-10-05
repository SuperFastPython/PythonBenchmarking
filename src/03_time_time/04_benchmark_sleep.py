# SuperFastPython.com
# example of benchmarking with sleep via time.time()
from time import time
from time import sleep
# record start time
time_start = time()
# execute the statement
data = [i*i for i in range(100000000)]
# sleep for a moment
sleep(2)
# record end time
time_end = time()
# calculate the duration
time_duration = time_end - time_start
# report the duration
print(f'Took {time_duration:.3f} seconds')
