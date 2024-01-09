"""
PROBLEM: Power Digit Sum
2^15 = 32768 and the sum of its digits is 26.
What is the sum of the digits of 2^1000
"""


def sum_of_digits(n: int) -> int:
    digits = [int(digit) for digit in str(n)]
    return sum(digits)


def solution(power: int) -> int:
    return sum_of_digits(2**power)


if __name__ == "__main__":
    print(solution(15))
    print(solution(1000))
