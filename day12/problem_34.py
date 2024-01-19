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
