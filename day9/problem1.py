# Self powers
# The series 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317
# what are the first 10 digits of the series ending at n=1000


def sum_of_n_power_n(n: int) -> int:
    total = 0

    for i in range(1, n + 1):
        total += i**i

    return total


def solution(n: int) -> int:
    number = sum_of_n_power_n(n)
