# SuperFastPython.com
# example of a program that executes tasks sequentially
from time import perf_counter
from time import sleep

# task function
def task(data):
    # block for a moment to simulate work
    sleep(1)

# do all the work
def main():
    # execute many tasks concurrently
    for i in range(20):
        task(i)

# protect the entry point
if __name__ == '__main__':
    # record start time
    time_start = perf_counter()
    # call benchmark code
    main()
    # calculate the duration
    time_duration = perf_counter() - time_start
    # report the duration
    print(f'Took {time_duration:.3f} seconds')
