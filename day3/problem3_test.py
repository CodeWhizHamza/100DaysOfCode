from day3.problem_7 import solution, is_prime


def test_is_prime():
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(4) is False
    assert is_prime(5) is True
    assert is_prime(6) is False
    assert is_prime(7) is True
    assert is_prime(8) is False
    assert is_prime(9) is False
    assert is_prime(10) is False
    assert is_prime(11) is True
    assert is_prime(12) is False
    assert is_prime(13) is True


def test_solution():
    assert solution(6) == 13
    # assert solution(10001)
