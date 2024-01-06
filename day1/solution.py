"""
PROBLEM:
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

MAX_NUMBER = 1000
total = 0

for i in range(MAX_NUMBER - 1, 0, -1):
    if i % 3 == 0 or i % 5 == 0:
        total += i

print(f"Sum of all the multiples of 3 and 5 below 1000 is {total}")
