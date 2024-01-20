# PROBLEM 30: Digit Fifth Powers


def statisfy_required_condition(number: int, power: int) -> bool:
    digits = [int(digit) for digit in str(number)]
    powers = [digit**power for digit in digits]
    return sum(powers) == number


def solution(power: int) -> int:
    sum_of_numbers: int = 0
    MAX_LIMIT = power * 9**power

    for i in range(2, MAX_LIMIT + 1):
        if statisfy_required_condition(i, power):
            sum_of_numbers += i

    return sum_of_numbers


if __name__ == "__main__":
    print(solution(4))
    print(solution(5))
