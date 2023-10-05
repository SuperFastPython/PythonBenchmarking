# SuperFastPython.com
# example of benchmarking a program with time.time()
from time import time

# function to benchmark
def task():
    # create a large list
    data = [i*i for i in range(100000000)]

# main function for program
def main():
    # call a function
    task()

# protect the entry point
if __name__ == '__main__':
    # record start time
    time_start = time()
    # execute the program
    main()
    # record end time
    time_end = time()
    # calculate the duration
    time_duration = time_end - time_start
    # report the duration
    print(f'Took {time_duration:.3f} seconds')
