"""
Problem: Summation of primes
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""


from math import sqrt


def is_prime(n: int) -> bool:
    if n <= 1:
        return False

    if n <= 3:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    max_limit = int(sqrt(n)) + 1
    for i in range(5, max_limit, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False

    return True


def solution(n: int) -> int:
    if n < 2:
        return 0

    if n == 2:
        return 2

    total = 2

    for i in range(3, n + 1, 2):
        if is_prime(i):
            total += i

    return total


if __name__ == "__main__":
    print(solution(10))
    print(solution(2_000_000))
