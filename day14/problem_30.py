# PROBLEM 30: Digit Fifth Powers


def sum_of_digits_to_the_power(number: int, power: int) -> int:
    digits = [int(digit) for digit in str(number)]
    powers = [digit**power for digit in digits]
    return sum(powers)
