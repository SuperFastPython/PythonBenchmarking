# SuperFastPython.com
# details of the clock used by perf_counter()
from time import get_clock_info
# get details
details = get_clock_info('perf_counter')
# report details
print(details)
