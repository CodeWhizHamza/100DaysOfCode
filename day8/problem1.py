# 1000-digit fibonacci number


def fib(n: int) -> int:
    if n <= 1:
        return n

    first = 0
    second = 1

    for i in range(n - 1):
        temp = second
        second = second + first
        first = temp

    return second
