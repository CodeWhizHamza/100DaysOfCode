from day3.problem_4 import is_palindrome, solution


def test_is_palindrome():
    assert is_palindrome(1) is True
    assert is_palindrome(10) is False
    assert is_palindrome(202) is True
    assert is_palindrome(9009) is True
    assert is_palindrome(205) is False
    assert is_palindrome(123456654321) is True


def test_solution():
    assert solution(1) == 9
    assert solution(2) == 9009
    assert solution(3) == 906609
