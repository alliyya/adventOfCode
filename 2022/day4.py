import math
"""
https://adventofcode.com/2022/day/4
Usage:
    cat day4_input.txt | python3 day4.py
        > The contents of the expense report:

    ou
    python3 day4.py
        input moves and ctrl-d (EOF) to end inputs
         > The contents of the expense report:
"""

def expand_selection(assignment):
    min, max = assignment.split("-")
    nums = list(range(int(min),int(max)+1))
    return nums


def camp_cleanup():
    line = input()
    fully_contained = 0
    partly_contained = 0

    while line:
        try:

            elf_1, elf_2 = line.split(",")  
            elf_1 = set(expand_selection(elf_1))
            elf_2 =set(expand_selection(elf_2))
            intersection = elf_1 & elf_2
            
            if (intersection == elf_1 or intersection == elf_2):
                fully_contained +=1
            elif intersection != set():
                partly_contained +=1
           
            line = input()
        except EOFError:
            break

    partly_contained += fully_contained

    print(f"Part 1: assignment pairs that are fully contained: {fully_contained}")
    print(f"Part 2: assignment pairs that are overlap: {partly_contained}")


def main():
    camp_cleanup()

if __name__ == '__main__':
    main()
