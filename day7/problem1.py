"""
PROBLEM: Highly Divisible Triangular Number
"""


from math import ceil, sqrt


def number_of_factors(number: int) -> int:
    if number <= 1:
        return 1

    count = 2  # 1 and the number are included

    for i in range(2, number // 2 + 1):
        if number % i == 0:
            count += 1

    return count


def solution(number_of_factors: int) -> int:
    pass


if __name__ == "__main__":
    print(solution(5))
    print(solution(500))
