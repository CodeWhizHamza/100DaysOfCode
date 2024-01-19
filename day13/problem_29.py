# Problem 29
"""
Combination of all integers for a^b where 2 <= a, b <= 5 are:
4, 8, 9, 16, 25, 27, 32, 64, 81, 125, 243, 256, 625, 1024, 31255.

How many combination can be made for this exacty sequence, if lower_limit is 2 and upper_limit is 100.f
"""

from typing import Set


def solution() -> int:
    numbers: Set[int] = set()

    for i in range(2, 101):
        for j in range(2, 101):
            numbers.add(i**j)

    return len(numbers)


if __name__ == "__main__":
    print(solution())
