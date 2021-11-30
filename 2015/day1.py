import math
"""
https://adventofcode.com/2015/day/1
Usage:
    cat day1_input.txt | python3 day1.py
        > The floor patterns are xxx

    ou
    python3 day1.py
        input numbers and ctrl-d (EOF) to end inputs
        > The floor patterns are xxx
"""

def part_1(sequence): 
    print(F"\nThe current floor is: {get_current_floor(sequence)}")

def get_current_floor(sequence: str):
    up = sequence.count("(")
    down = sequence.count(")")
    
    return up-down

def part_2(sequence):
    print(F"The basement is entered on step: {get_basement_pos(sequence)}")


def get_basement_pos(sequence):
    current_floor = 0
    count = 0
    for x in sequence:
        if x=="(":
            current_floor +=1
        else:
            current_floor -=1
        count += 1
        if current_floor == -1:
            return count



def main():
    sequence = input("The floor patterns are:")
    
    part_1(sequence)
    part_2(sequence)

 

if __name__ == '__main__':
    main()
