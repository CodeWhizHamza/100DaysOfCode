from problem1 import factorial, solution, sum_of_digits


def test_factorial():
    assert factorial(1) == 1
    assert factorial(5) == 120


def sum_of_digits():
    assert sum_of_digits(100) == 1
    assert sum_of_digits(123) == 6


def test_solution():
    assert solution(10) == 27
    assert solution(100) == 648
