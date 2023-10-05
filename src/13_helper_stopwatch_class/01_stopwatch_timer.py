# SuperFastPython.com
# example of a custom stopwatch timer class
from time import perf_counter

# custom stopwatch timer class
class StopwatchTimer:
    # start the timer
    def start(self):
        self.time_start = perf_counter()
    # stop the timer
    def stop(self):
        self.time_end = perf_counter()
    # get the duration
    def duration(self):
        return self.time_end - self.time_start

# create the timer
timer = StopwatchTimer()
# start the timer
timer.start()
# create a list of squared numbers
result = [i*i for i in range(100000000)]
# stop the timer
timer.stop()
# report the duration
print(f'Took {timer.duration()} seconds')
