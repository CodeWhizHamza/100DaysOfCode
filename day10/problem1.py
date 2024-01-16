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


if __name__ == "__main__":
    print(is_abundant(1))
    print(is_abundant(16))
    print(is_abundant(12))
    print(is_abundant(24))
