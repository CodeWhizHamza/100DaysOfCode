from problem2 import is_palindrome, solution


def test_is_palindrome():
    assert is_palindrome(1) == True
    assert is_palindrome(10) == False
    assert is_palindrome(202) == True
    assert is_palindrome(9009) == True
    assert is_palindrome(205) == False
    assert is_palindrome(123456654321) == True


def test_solution():
    assert solution(1) == 9
    assert solution(2) == 9009
