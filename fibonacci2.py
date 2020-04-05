# Fibonacci with memoization through an imported module

from functools import lru_cache


@lru_cache(maxsize=1000)
def fibonacci(n):
    # Check that the input is an integer
    if type(n) != int:
        raise TypeError("n must be a positive integer")
    if n < 1:
        raise ValueError("n must be a positive integer")

    # Compute the Nth term
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)


for n in range(1, 1501):
    print(n, ":", fibonacci(n))
