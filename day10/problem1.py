# Non abundant Sums

from typing import List


def get_factors(n: int) -> List[int]:
    factors = [1]

    for number in range(2, n // 2):
        if n % number == 0:
            factors.append(number)

    return factors


if __name__ == "__main__":
    print(get_factors(1))
    print(get_factors(28))
