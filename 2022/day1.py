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
    total = 0 + num
    max = 0
    while num:
        try:
            num = int(input())
            total += num
        except ValueError:
            if total > max:
                max = total
            total = 0
        except EOFError:
            break
    print(max)


def part_2():
    num = int(input())
    total = 0 + num
    totals = []
    while num:
        try:
            num = int(input())
            total += num
        except ValueError:
            totals.append(total)
            total = 0
        except EOFError:
            totals.append(total)
            break
    totals.sort(reverse=True)
    print(sum(totals[:3]))



def main():
    # part_1()
    part_2()


if __name__ == '__main__':
    main()
