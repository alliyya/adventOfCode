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


def part_1():
    num = int(input())
    sum = 0
    while num:
        sum += num

        try:
            num = int(input())
        except EOFError:
            break

    print(F"Resulting frequency after all of the changes in frequency: {sum}")


def part_2():
    num = int(input())
    sum = 0
    numbers = []
    repeated = None
    frequencies = []
    while num:
        numbers.append(num)
        sum += num
        frequencies.append(sum)
        try:
            num = int(input())
        except EOFError:
            break

    i = 0
    while not repeated:
        sum += numbers[i]

        if i == len(numbers)-1:
            i = 0
        else:
            i += 1

        if sum in frequencies:
            repeated = sum

    print(F"First frequency your device reaches twice: {repeated}")


def main():
    # part_1()
    part_2()


if __name__ == '__main__':
    main()
