from day5.problem_16 import solution, sum_of_digits


def test_sum_of_digits():
    assert sum_of_digits(1234) == 10
    assert sum_of_digits(32768) == 26


def test_solution():
    assert solution(15) == 26
