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


def part_1():
    num = int(input())
    increases = 0
    while num:
        prev_num = num
        try:
            num = int(input())
        except EOFError:
            break
        if num > prev_num:
            increases += 1
    print(
        F"There are {increases} measurements that are larger than the previous measurement")


def part_2():
    num = int(input())
    a = 0
    b = 0
    c = 0
    increases = 0
    sum = 0
    prev_sum = 0

    while num:
        if a == 0:
            a = num
        elif b == 0:
            b = num
        elif c == 0:
            c = num
        else:
            a = b
            b = c
            c = num

        if prev_sum == 0 and a and b and c:
            prev_sum = a + b + c
            sum = a + b + c
        elif a and b and c:
            prev_sum = sum
            sum = a + b + c

        if sum > prev_sum:
            increases += 1

        try:
            num = int(input())
        except EOFError:
            break

    print(F"There are {increases} sums that are larger than the previous sums")


def main():
    # part_1()
    part_2()


if __name__ == '__main__':
    main()
