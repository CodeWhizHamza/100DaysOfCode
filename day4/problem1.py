"""
A pythagorean triplet is a set of three natural numbers a < b < c for which,
a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 5^2
There exists exactly one Pyatagoran triplet for which a + b + c = 1000.
Find the product of abc
"""


def is_pythagorean_triplet(x: int, y: int, z: int) -> bool:
    return x < y < z and (x**2 + y**2) == z**2


def solution() -> int:
    for i in range(1, 999):
        for j in range(i, 999):
            for k in range(j, 999):
                if (i + j + k) == 1000 and is_pythagorean_triplet(i, j, k):
                    return i * j * k

    return 0


if __name__ == "__main__":
    print(solution())
