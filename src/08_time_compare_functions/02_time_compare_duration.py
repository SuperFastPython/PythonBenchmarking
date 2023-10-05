# SuperFastPython.com
# example of timing a statement with each timing method
from time import time
from time import perf_counter
from time import monotonic
from time import process_time
from time import thread_time
# record start times
s1 = time()
s2 = perf_counter()
s3 = monotonic()
s4 = process_time()
s5 = thread_time()
# execute the statement
data = [i*i for i in range(100000000)]
# record end times
e1 = time()
e2 = perf_counter()
e3 = monotonic()
e4 = process_time()
e5 = thread_time()
# calculate the durations
d1 = e1 - s1
d2 = e2 - s2
d3 = e3 - s3
d4 = e4 - s4
d5 = e5 - s5
# report the durations
print(f'time:         {d1}')
print(f'perf_counter: {d2}')
print(f'monotonic:    {d3}')
print(f'process_time: {d4}')
print(f'thread_time:  {d5}')
