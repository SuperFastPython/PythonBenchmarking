# SuperFastPython.com
# details of the clock used by monotonic()
from time import get_clock_info
# get details
details = get_clock_info('monotonic')
# report details
print(details)
