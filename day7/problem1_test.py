from problem1 import number_of_factors, solution


def test_number_of_factors():
    assert number_of_factors(1) == 1
    assert number_of_factors(2) == 2
    assert number_of_factors(6) == 4
    assert number_of_factors(28) == 6


def test_solution():
    assert solution(5) == 28
    assert solution(500) == 0
