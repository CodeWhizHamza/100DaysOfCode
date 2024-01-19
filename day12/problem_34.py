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


def is_curious_number(n: int) -> bool:
    digits = [int(d) for d in str(n)]
    sum_of_digits_factorial = sum([factorial(digit) for digit in digits])
    return n == sum_of_digits_factorial


if __name__ == "__main__":
    pass
