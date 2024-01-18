# problem 36
# Double base palindromes


def is_palindrome(n) -> bool:
    return str(n) == str(n)[::-1]


def solution(high_limit: int) -> int:
    """This function solves the  problem 36 of Project Euler

    Args:
        high_limit (int): upper limit exclusive

    Returns:
        int: sum of all the palindromic numbers in both bases
    """
    total: int = 0

    for i in range(1, high_limit):
        if is_palindrome(i) and is_palindrome(bin(i)[2:]):
            print(i)
            total += i

    return total
