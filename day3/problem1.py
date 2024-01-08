"""
PROBLEM:
The prime factors of 13195 are 5, 7, 13, and 29.
What is the largest prime factor of the number 600851475143
"""


from math import sqrt


class UnableToProcessNegativeNumbers(Exception):
    ...


def is_prime(n: int) -> bool:
    if n == 1:
        return False

    if n < 0:
        raise UnableToProcessNegativeNumbers()

    for i in range(2, int(sqrt(n) + 1)):
        if n % i == 0:
            return False

    return True


def solution(n: int) -> int:
    largest = 1

    for i in range(1, int(sqrt(n))):
        if not is_prime(i):
            continue

        if n % i == 0 and largest < i:
            largest = i

    return largest


if __name__ == "__main__":
    print(solution(13195))
    print(solution(600851475143))
    print(is_prime(35))
