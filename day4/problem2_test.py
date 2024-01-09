from problem2 import solution, product


def test_product():
    assert product("9989") == 5832
    assert product("1234") == 24


def test_solution():
    assert solution(4) == 5832
    assert solution(13) == 23514624000
