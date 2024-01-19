# Problem 29
"""
Combination of all integers for a^b where 2 <= a, b <= 5 are:
4, 8, 9, 16, 25, 27, 32, 64, 81, 125, 243, 256, 625, 1024, 31255.

How many combination can be made for this exacty sequence, if lower_limit is 2 and upper_limit is 100.f
"""

from typing import Set


def solution(lower_limit: int, upper_limit: int) -> int:
    numbers: Set[int] = set()

    for i in range(lower_limit, upper_limit + 1):
        for j in range(lower_limit, upper_limit + 1):
            numbers.add(i**j)

    return len(numbers)


if __name__ == "__main__":
    print(solution(2, 100))
