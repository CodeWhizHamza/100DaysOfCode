# PROBLEM 30: Digit Fifth Powers


def statisfy_required_condition(number: int, power: int) -> int:
    digits = [int(digit) for digit in str(number)]
    powers = [digit**power for digit in digits]
    return sum(powers) == number
