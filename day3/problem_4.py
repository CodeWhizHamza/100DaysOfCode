"""
PROBLEM: Largest palindrome product
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2 digit numbers is 9009 = 91 * 99.
Find the largest palindrome made from the product of 3 digit numbers.
"""


class CannotAcceptNonPositiveNumbers(Exception):
    ...


def is_palindrome(n: int) -> bool:
    return str(n)[::-1] == str(n)


def solution(number_of_digits: int) -> int:
    if number_of_digits <= 0:
        raise CannotAcceptNonPositiveNumbers()

    max_limit = 10**number_of_digits - 1

    largest_palindrome = 1

    for i in range(1, max_limit + 1):
        for j in range(1, max_limit + 1):
            product = i * j
            if is_palindrome(product) and product > largest_palindrome:
                largest_palindrome = product

    return largest_palindrome


if __name__ == "__main__":
    print(solution(2))
    print(solution(3))
