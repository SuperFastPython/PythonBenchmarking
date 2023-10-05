# SuperFastPython.com
# example of benchmarking list of numbers with timeit()
from timeit import timeit
# benchmark the i*i method
time_method1 = timeit('[i*i for i in range(1000)]',
    number=100000)
# report the duration
print(f'i*i: {time_method1:.3f} seconds')
# benchmark the i**2 method
time_method2 = timeit('[i**2 for i in range(1000)]',
    number=100000)
# report the duration
print(f'i**2: {time_method2:.3f} seconds')
