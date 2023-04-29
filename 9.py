from functools import lru_cache
from timeit import default_timer


@lru_cache
def fib1(n):
    if n <= 2:
        return 1
    return fib1(n - 1) + fib1(n - 2)


cache = {}


def fib2(n):
    if n <= 2:
        return 1
    if n not in cache:
        cache[n] = fib2(n - 1) + fib2(n - 2)
        return cache[n]
    return cache[n]


if __name__ == '__main__':
    start = default_timer()
    print(fib1(100))  # 1 1 2 3 5
    middle = default_timer()
    print(fib2(100))
    end = default_timer()
    print(f"lru_cache-{middle - start:f}, dict-{end - middle:f}")
