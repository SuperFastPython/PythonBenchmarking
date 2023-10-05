# SuperFastPython.com
# details of the clock used by process_time()
from time import get_clock_info
# get details
details = get_clock_info('process_time')
# report details
print(details)
