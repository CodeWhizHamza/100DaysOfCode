from day2.problem_2 import fib, solution


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(3) == 2
    assert fib(4) == 3
    assert fib(10) == 55


def test_solution():
    assert solution(10) == 10
    assert solution(5) == 2
    assert solution(89) == 44
    assert solution(4_000_000) == 4613732
