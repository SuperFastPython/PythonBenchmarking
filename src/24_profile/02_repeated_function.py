# SuperFastPython.com
# example of a program that calls a function repeatedly
import math

# long running task
def work():
    # block the main thread for a long time
    data = [math.sqrt(i) for i in range(1, 100000000)]

# main program
def main():
    # report a message
    print('Main is running')
    # run our task
    work()
    # report a message
    print('Main is done.')

# protect the entry point
if __name__ == '__main__':
    # start the program
    main()
