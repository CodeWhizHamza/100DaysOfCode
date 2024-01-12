from problem3 import solution


def test_solution():
    assert solution(13) == 9
    assert solution(1_000_000) == 837799
