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

    for i in range(2, int(sqrt(n))):
        if n % i == 0:
            return False

    return True


def solution(n: int) -> int:
    pass


if __name__ == "__main__":
    print(solution(13195))
    print(solution(600851475143))
