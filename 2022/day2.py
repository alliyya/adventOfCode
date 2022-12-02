import math
"""
https://adventofcode.com/2020/day/2
Usage:
    cat day2_input.txt | python3 day2.py
        > The contents of the expense report:

    ou
    python3 day2.py
        input moves and ctrl-d (EOF) to end inputs
         > The contents of the expense report:
"""

point_map = {
    "X": 1, # rock
    "Y": 2, # paper
    "Z": 3,  #scissor
    "A": 1, # rock
    "B": 2, # paper
    "C": 3,  #scissor
}

# There's probably a more optimal way to calculate win/loss
scoring = {
    "A": {"win":"Y","lose": "Z"},  # Rock --> Paper (1,2)
    "B": {"win":"Z","lose": "X"},  # Paper --> Scissors (2,3)
    "C": {"win":"X","lose": "Y"},  # Scissors --> Rock (3,1)
}

def calc_score(elf_move, my_move):
        if point_map[elf_move] == point_map[my_move]:  # tie
            return 3 + point_map[my_move]
        elif my_move == scoring[elf_move]["win"]: # I win
            return 6 + point_map[my_move]
        else: # I lose
            return point_map[my_move]


def part_1():
    elf_move,my_move = input().split()
    total_score = 0

    while elf_move+my_move:
        try:
            total_score += calc_score(elf_move, my_move)
            elf_move, my_move = input().split()
        except EOFError:
            break

    print(total_score)


def part_2():
    elf_move, my_move = input().split()
    total_score = 0

    while elf_move+my_move:
        try:
            if my_move == 'Z': # win
                my_move = scoring[elf_move]["win"]
            elif my_move == 'Y': # tie
                my_move = elf_move
            else: # lose
                my_move = scoring[elf_move]["lose"]
                        
            total_score += calc_score(elf_move, my_move)
            elf_move, my_move = input().split()
        except EOFError:
            break

    print(total_score)



def main():
    part_1()
    # part_2()


if __name__ == '__main__':
    main()
