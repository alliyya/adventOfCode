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


def part_1():
    
    y = 0
    x = 0
    step = input("The steps are:")
    while step:
        position = step.split(" ")
        if position[0] == "forward":
            x += int(position[1])
        elif position[0] == "down":
            y += int(position[1])
        elif position[0] == "up":
            y -= int(position[1])




        try:
            step = input()
        except EOFError:
            break

    print(
        F"The quotient of final horizontal position and final depth is {x}x{y} = {x*y}")


def part_2():
    y = 0
    x = 0
    aim = 0
    step = input("The steps are:")
    while step:
        position = step.split(" ")
        if position[0] == "forward":
            x += int(position[1])
            y += aim*int(position[1])
        elif position[0] == "down":
            aim += int(position[1])
        elif position[0] == "up":
            aim -= int(position[1])

        try:
            step = input()
        except EOFError:
            break

    print(
        F"The quotient of final horizontal position and final depth is {x}x{y} = {x*y}")



def main():
    # part_1()
    part_2()


if __name__ == '__main__':
    main()
