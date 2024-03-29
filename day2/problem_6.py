"""
PROBLEM: Sum square difference
The sum of squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of first 10 natural numbers is, 
(1 + 2 + ... + 10) ^ 2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is,
3025 - 385 = 2640
Find the difference between the sum of the squares of the first one hundred natural numbers and the squares of the sum.
"""


def sum_of_squares_of(n: float) -> float:
    return n * (n + 1) * (2 * n + 1) / 6


def square_of_sum_of(n: float) -> float:
    return (n * (n + 1) / 2) ** 2


def solution(n: float) -> float:
    return abs(square_of_sum_of(n) - sum_of_squares_of(n))


if __name__ == "__main__":
    print(solution(10))
    print(solution(100))
