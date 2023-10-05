# SuperFastPython.com
# example of a custom stopwatch timer class with resume support
from time import perf_counter

# custom stopwatch timer class that can be resumed
class ResumeStopwatchTimer:
    # constructor
    def __init__(self):
        self.reset()
    # start or resume the timer
    def start(self):
        self.time_start = perf_counter()
    # stop the timer
    def stop(self):
        time_end = perf_counter()
        self.sum_duration += time_end - self.time_start
    # get the duration
    def duration(self):
        return self.sum_duration
    # reset the timer
    def reset(self):
        self.sum_duration = 0

# create the timer
timer = ResumeStopwatchTimer()
# start the timer
timer.start()
# create a list of squared numbers
result = [i*i for i in range(100000000)]
# stop the timer
timer.stop()
# report the duration
print(f'Took {timer.duration()} seconds')
# resume the timer
timer.start()
# do some more work
result = [i*i for i in range(100000000)]
# stop the timer
timer.stop()
# report the duration
print(f'Took {timer.duration()} seconds')
