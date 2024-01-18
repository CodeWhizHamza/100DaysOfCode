# problem 36
# Double base palindromes

from typing import TypeVar


T = TypeVar("T")


def is_palindrome(n: T) -> bool:
    return str(n) == str(n)[::-1]
