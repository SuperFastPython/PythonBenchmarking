# SuperFastPython.com
# example of benchmarking list of numbers with timeit()
from timeit import timeit

# define a custom function for squaring numbers
def square(value):
    return value * value

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
# benchmark the math.pow() method
time_method3 = timeit('[pow(i,2) for i in range(1000)]',
    setup='from math import pow', number=100000)
# report the duration
print(f'math.pow(): {time_method3:.3f} seconds')
# benchmark the square() method
time_method4 = timeit(
    '[square(i) for i in range(1000)]',
    globals=globals(), number=100000)
# report the duration
print(f'square(): {time_method4:.3f} seconds')
