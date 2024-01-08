"""
PROBLEM:
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that 6th prime is 13.
What is the 10001st prime number?
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
    if n < 0:
        raise UnableToProcessNegativeNumbers()

    number_count = 1
    current_number = 2
    current_prime_number = 0
    while True:
        if number_count == n + 1:
            return current_prime_number

        if is_prime(current_number):
            current_prime_number = current_number
            number_count += 1

        current_number += 1


if __name__ == "__main__":
    print(solution(6))
    print(solution(10001))
