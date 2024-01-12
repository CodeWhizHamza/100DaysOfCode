"""
PROBLEM: Factorial digit sum
"""


def factorial(number: int) -> int:
    result = 1

    if number <= 1:
        return 1

    for i in range(1, number + 1):
        result *= i

    return result


def sum_of_digits(number: int) -> int:
    pass


def solution(number: int) -> int:
    pass


if __name__ == "__main__":
    print(solution(10))
    print(solution(100))
