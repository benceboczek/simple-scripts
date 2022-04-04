from contextlib import contextmanager
import time


@contextmanager
def timed():
    start_time = time.time()
    yield
    end_time = time.time()
    print("Total execution time: {}".format(end_time - start_time))


def cached(func):
    cache = {}
    def inner(*args, **kwargs):
        if args in cache.keys():
            print("--- already in cache ---")
            return cache.get(args)
        else:
            print("--- first call, cached ---")
            cache[args] = func(*args, **kwargs)
            return cache[args]

    return inner


@cached
def factorial(n):
    r = 1
    i = 2
    while i <= n:
        r *= i
        i += 1
    return r


def main():
    with timed():
          for i in range(5000):
            factorial(3000 + (i % 50))


if __name__ == '__main__':
    main()
