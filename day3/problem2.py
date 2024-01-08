"""
PROBLEM:
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2 digit numbers is 9009 = 91 * 99.
Find the largest palindrome made from the product of 3 digit numbers.
"""


def is_palindrome(n: int) -> bool:
    return str(n)[::-1] == str(n)


def solution(number_of_digits: int) -> int:
    pass


if __name__ == "__main__":
    print(solution(2))
    print(solution(3))
