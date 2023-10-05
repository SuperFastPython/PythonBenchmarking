# SuperFastPython.com
# example of a program that executes tasks concurrently
from time import time
from time import sleep
from concurrent.futures import ThreadPoolExecutor

# task function
def task(data):
    # block for a moment to simulate work
    sleep(1)

# do all the work
def main():
    # create the thread pool
    n = 20
    with ThreadPoolExecutor(n) as tpe:
        # issue all tasks
        _ = [tpe.submit(task, i) for i in range(n)]
    # wait for all tasks to complete

# protect the entry point
if __name__ == '__main__':
    # record start time
    time_start = time()
    # call benchmark code
    main()
    # calculate the duration
    time_duration = time() - time_start
    # report the duration
    print(f'Took {time_duration:.3f} seconds')
