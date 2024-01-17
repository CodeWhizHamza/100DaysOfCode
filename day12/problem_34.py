# Digit Factorials
# 145 is a curious number as the sum of factorials of its digits is equal to 145.
# find the sum of all numbers


def factorial(n: int) -> int:
    if n <= 1:
        return 1

    value = 1
    for i in range(2, n + 1):
        value *= i
    return value


FACTORIAL_OF_FIRST_10_NUMBERS = [factorial(i) for i in range(10)]


def is_curious_number(n: int) -> bool:
    digits = [int(d) for d in str(n)]
    sum_of_digits_factorial = sum(
        [FACTORIAL_OF_FIRST_10_NUMBERS[digit] for digit in digits]
    )
    return n == sum_of_digits_factorial


def solution():
    total = 0
    for i in range(3, 10000000):
        if is_curious_number(i):
            total += i

    return total


if __name__ == "__main__":
    print(solution())
