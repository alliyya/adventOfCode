import math
"""
https://adventofcode.com/2020/day/1
Usage:
    cat day1_input.txt | python3 day1.py
        > The contents of the expense report:

    ou
    python3 day1.py
        input numbers and ctrl-d (EOF) to end inputs
         > The contents of the expense report:
"""


def part_1(sequence):
    print(F"\nThe quotient is: {get_quotient(sequence)}")


def get_quotient(sequence: list):
# Would not scale for multiple numbers to be summed
    for x in sequence:
        y = 2020 - x
        if y in sequence:
            return x*y

def main():
    numbers = []
    num = int(input())
    while num:
        numbers.append(num)
        try:
            num = int(input())
        except EOFError:
            break

    part_1(numbers)


if __name__ == '__main__':
    main()
