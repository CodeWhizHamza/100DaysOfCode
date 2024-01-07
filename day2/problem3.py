"""
PROBLEM:
2520 is the smallest number than can be divided by the each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""


def is_evenly_divisible_by(number: float, max_divider: float) -> bool:
    for i in range(1, int(max_divider) + 1):
        if number % i != 0:
            return False

    return True


def solution(max_divider: float) -> float:
    number = 2520
    while not is_evenly_divisible_by(number, max_divider):
        number += 2520

    return number


if __name__ == "__main__":
    print(solution(10))
    print(solution(20))
