"""
PROBLEM:
Each new term in the Fibonacci sequence is generate by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
1, 2, 3, 5, 8, 13, 21, 24, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even valued terms.
"""


from typing import Dict


def fib(n: int) -> int:
    cache: Dict[int, int] = {}

    def fib_with_cache(n: int) -> int:
        if n <= 1:
            return n

        cached_value = cache.get(n, None)
        if cached_value is None:
            cache[n] = fib_with_cache(n - 1) + fib_with_cache(n - 2)
        return cache[n]

    return fib_with_cache(n)


def solution(max_limit: int) -> int:
    total = 0
    i = 0
    while True:
        value = fib(i)
        if value > max_limit:
            break

        if value % 2 == 0:
            total += value
        i += 1

    return total


if __name__ == "__main__":
    print(solution(4000000))
