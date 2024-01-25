from day4.problem_10 import solution, is_prime


def test_is_prime():
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(4) is False
    assert is_prime(1) is False
    assert is_prime(13) is True
    assert is_prime(20) is False


def test_solution():
    assert solution(10) == 17
    assert solution(2_000_000) == 142913828922
