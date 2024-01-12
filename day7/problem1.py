"""
PROBLEM: Highly Divisible Triangular Number
"""


def number_of_factors(number: int) -> int:
    if number <= 1:
        return 1

    count = 2  # 1 and the number are included

    for i in range(2, number // 2 + 1):
        if number % i == 0:
            count += 1

    return count


def solution(factors_count: int) -> int:
    triangular_number = 1
    current_natural_number = 2

    while True:
        if number_of_factors(triangular_number) > factors_count:
            return triangular_number

        triangular_number += current_natural_number
        current_natural_number += 1


if __name__ == "__main__":
    print(solution(5))
    print(solution(500))
