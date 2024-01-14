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


def solution(n: int, verbose: bool = True) -> int:
    i = 1
    while True:
        number = fib(i)

        if len(str(number)) == n:
            break

        i += 1

    if verbose:
        print(f"Index of fib number with {n} digits is {i}")
    return i


if __name__ == "__main__":
    solution(3)
    solution(1000)
