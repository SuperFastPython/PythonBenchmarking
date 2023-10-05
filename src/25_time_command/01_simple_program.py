# SuperFastPython.com
# example of a python program that can be benchmarked

# function to benchmark
def task():
    # create a large list
    data = [i*i for i in range(100000000)]

# protect the entry point
if __name__ == '__main__':
    # run the task
    task()
