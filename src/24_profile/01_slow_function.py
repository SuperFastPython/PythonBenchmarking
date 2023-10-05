# SuperFastPython.com
# example of a program that has a slow function call
import time

# long running task
def work():
    # block the thread for a long time
    time.sleep(5)

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
