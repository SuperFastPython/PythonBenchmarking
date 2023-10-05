# SuperFastPython.com
# example of benchmarking a program with perf_counter()
from time import perf_counter

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
    time_start = perf_counter()
    # execute the program
    main()
    # record end time
    time_end = perf_counter()
    # calculate the duration
    time_duration = time_end - time_start
    # report the duration
    print(f'Took {time_duration:.3f} seconds')
