# SuperFastPython.com
# report the details of each time function
from time import get_clock_info
# time.time()
print(get_clock_info('time'))
# time.perf_counter()
print(get_clock_info('perf_counter'))
# time.monotonic()
print(get_clock_info('monotonic'))
# time.process_time()
print(get_clock_info('process_time'))
# time.thread_time()
print(get_clock_info('thread_time'))
