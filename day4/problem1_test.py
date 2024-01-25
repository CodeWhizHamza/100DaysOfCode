from day4.problem_9 import solution, is_pythagorean_triplet


def test_is_pythagorean_triplet():
    assert is_pythagorean_triplet(3, 4, 5) is True
    assert is_pythagorean_triplet(1, 2, 3) is False


def test_solution():
    assert solution() == 31875000
