import math
"""
https://adventofcode.com/2015/day/1
Usage:
    cat day1_input.txt | python3 day1.py
        > The steps are: xxx

    ou
    python3 day1.py
        input numbers and ctrl-d (EOF) to end inputs
        > The steps are: xxx
"""


def part_1(report):
    transposed_report = transpose_list(report)
    gamma_rate = ""
    for x in transposed_report:
        if x.count('1') > x.count('0'):
            gamma_rate += "1"
        else:
            gamma_rate += "0"

    epsilon_rate = gamma_rate.replace(
        '1', '2').replace('0', '1').replace('2', '0')
    print(
        F"\nPower consumption of the submarine: {int(gamma_rate,2)*int(epsilon_rate,2)}")


def part_2(report):
    oxygen_generator_rating = get_rating(report, 1)
    co2_scrubber_rating = get_rating(report, 0)
    print(
        F"Life support rating of the submarine: {oxygen_generator_rating*co2_scrubber_rating}")


def print_list(listy):
    string = ""
    for x in range(len(listy)):
        item = listy[x]
        string = F"{x+1}: {item}--> 1:{item.count('1')}, 0:{item.count('0')} "
        print(string)


def transpose_list(listy):
    return [list(i) for i in zip(*listy)]


def get_rating(report, default):
    keep = None
    transposed_report = transpose_list(report)
    for x in range(len(transposed_report)):
        if transposed_report[x].count('1') >= transposed_report[x].count('0'):
            keep = str(default)
        else:
            keep = str(abs(default-1))

        # Keeping bits that pass the criteria
        report = [line for line in report if line[x] == keep]
        transposed_report = transpose_list(report)

        # Final bit determined
        if len(report) == 1:
            num = int(''.join(report[0]), 2)
            return num


def main():
    report = []
    line = input("The diagnostic report is:")
    while line:
        report.append(list(line))

        try:
            line = input()
        except EOFError:
            break

    part_1(report)
    part_2(report)


if __name__ == '__main__':
    main()
