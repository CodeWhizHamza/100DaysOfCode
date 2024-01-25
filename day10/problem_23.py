# Non abundant Sums

from typing import List


def get_factors(n: int) -> List[int]:
    factors = [1]

    for number in range(2, n // 2 + 1):
        if n % number == 0:
            factors.append(number)

    return factors


def is_abundant(n: int) -> bool:
    factors = get_factors(n)
    sum_of_factors = sum(factors)
    return sum_of_factors > n


def is_sum_of_two_abundant_numbers(n: int) -> bool:
    for i in range(n):
        if not is_abundant(i):
            continue
        for j in range(n):
            if not is_abundant(j):
                continue

            if n == i + j:
                return True

    return False


def solution() -> int:
    UPPER_LIMIT = 28123
    all_abundant_numbers = set()

    for i in range(1, UPPER_LIMIT):
        if is_abundant(i):
            all_abundant_numbers.add(i)

    total = 0

    for i in range(1, UPPER_LIMIT):
        if not any((i - a in all_abundant_numbers) for a in all_abundant_numbers):
            total += i

    return total


if __name__ == "__main__":
    print(solution())
