from multiprocessing import Pool
import time

# Multiprocessing is slower for short calculations.
# It starts being faster for calculations which take >1minute. When calculate fibonacci for number 21 and higher.


# Fibonacci function
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def multi(n: int):
    print(f'Multi - START')
    time_start = time.time()
    workers_count = 4
    pool = Pool(processes=workers_count)  # start 4 worker processes
    res = pool.apply_async(fibonacci, (n,))  # evaluate
    result = res.get()
    time_end = time.time()
    print(f"Multi - END: ({result}) " + str(time_end - time_start))


def plain(n: int):
    print(f'Plain - START')
    time_start = time.time()
    result = fibonacci(n)
    time_end = time.time()
    print(f"Multi - END: ({result}) " + str(time_end - time_start))


number = 41
plain(number)
multi(number)
