import math
"""
https://adventofcode.com/2019/day/1
Usage:
    cat day1_input.txt | python3 day1.py
        > The fuel requirements are xxx

    ou
    python3 day1.py
        input numbers and ctrl-d (EOF) to end inputs
        > The fuel requirements are xxx
"""


def calculate_fuel(fuel):
    fuel = math.floor(fuel / 3.0) - 2.0
    if fuel <= 0:
        return 0
    else:
        return fuel + calculate_fuel(fuel)


def main():
    total_fuel = 0
    mass = 0
    mass = int(input())
    while mass:

        total_fuel += calculate_fuel(mass)

        # This statement is from part 1.
        # total_fuel += math.floor(mass / 3.0) - 2.0
        try:
            mass = int(input())
        except EOFError:
            break

    print("The fuel requirements are " + str(total_fuel))


if __name__ == '__main__':
    main()
