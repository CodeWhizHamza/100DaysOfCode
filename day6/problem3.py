"""
PROBLEM: Longest Collatz Sequence
"""


def numbers_in_collatz_sequence_for(number: int) -> int:
    if number < 0:
        return 0

    count = 1

    while number != 1:
        if number % 2 == 0:
            number //= 2
        else:
            number = 3 * number + 1
        count += 1

    return count


def solution(max_limit: int) -> int:
    number_with_largest_chain = 0
    largest_count = 0

    for i in range(1, max_limit):
        current_count = numbers_in_collatz_sequence_for(i)
        if current_count > largest_count:
            largest_count = current_count
            number_with_largest_chain = i

    return number_with_largest_chain


if __name__ == "__main__":
    print(solution(13))
    print(solution(1_000_000))
