# SuperFastPython.com
# example of running a function in a new coroutine
import asyncio

# task that blocks for a moment and prints a message
async def task():
    # block for a moment
    await asyncio.sleep(1)
    # display a message
    print('This is coming from another coroutine')

# demonstrate executing a task in a coroutine
async def main():
    print('Waiting for the new coroutine to finish...')
    # run task and wait for it to complete
    await task()

# start the event loop
asyncio.run(main())
