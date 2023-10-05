# SuperFastPython.com
# details of the clock used by thread_time()
from time import get_clock_info
# get details
details = get_clock_info('thread_time')
# report details
print(details)
