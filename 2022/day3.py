import math
"""
https://adventofcode.com/2020/day/3
Usage:
    cat day3_input.txt | python3 day3.py
        > The contents of the expense report:

    ou
    python3 day3.py
        input moves and ctrl-d (EOF) to end inputs
         > The contents of the expense report:
"""

def calculate_priority(item_type):
    ascii_val = ord(item_type)
    
    if ascii_val >= 97:
        return ascii_val-96
    else:
        return ascii_val-65+27

def part_1():
    line = input()
    priority_sum = 0

    while line:
        try:
            rucksack_1 = set(line[:int(len(line)/2)])
            rucksack_2 = set(line[int(len(line)/2):])
            item_type = list(rucksack_1 & rucksack_2)[0]
            
            priority_sum += calculate_priority(item_type)
            
            line = input()
        except EOFError:
            break

    print(priority_sum)


def part_2():
    line1 = input()
    line2 = input()
    line3 = input()
    priority_sum = 0

    while line1 and line2 and line3:
        try:
            rucksack_1 = set(line1)
            rucksack_2 = set(line2)
            rucksack_3 = set(line3)
            item_type = list(rucksack_1 & rucksack_2 & rucksack_3)[0]
            
            priority_sum += calculate_priority(item_type)
            
            line1 = input()
            line2 = input()
            line3 = input()
        except EOFError:
            break

    print(priority_sum)




def main():
    # part_1()
    part_2()


if __name__ == '__main__':
    main()
