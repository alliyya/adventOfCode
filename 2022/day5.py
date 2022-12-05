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


def parse_config(configuration):
    configuration.reverse()
    stack_labels = configuration[0].split()
    col_count = stack_labels[-1]
    indices = [configuration[0].index(x) for x in stack_labels]
    stack = [[] for x in indices]

    for line in configuration[1:]:
        for stack_id, index in enumerate(indices):
            if (line[index] != " "):
                stack[stack_id].append(line[index])
    return stack

def cargo_crane():
    import copy

    line = input()
    configuration = []
    rearrangement = []

    while line:
        if line[0] == 'm':
            rearrangement.append(line)
        else:
            configuration.append(line)
    
        try:
            line = input()
        except EOFError:
            break

        if line == "":
            line = input()
        

    stack_1 = parse_config(copy.deepcopy(configuration))
    stack_2 = parse_config(configuration)
    instructions = [ parse_instruction(x) for x in rearrangement ]

    print("Part 1:","".join([x[-1] for x in part_1(stack_1, instructions)]))
    print("Part 2:","".join([x[-1] for x in part_2(stack_2, instructions)]))


def part_2(stack, instructions):
    for x in instructions:
        stack[x["end"]] += (stack[x["start"]][-x["quantity"]:])
        del stack[x["start"]][-x["quantity"]:]
    return stack

def part_1(stack, instructions):
    for x in instructions:
        length = len(stack[x["start"]])
        stack[x["start"]].reverse()

        stack[x["end"]]+=(stack[x["start"]][0:x["quantity"]])
        del stack[x["start"]][0:x["quantity"]]
        stack[x["start"]].reverse()
    return stack

def parse_instruction(instruction):
    parts = instruction.split("from")
    quantity = int(parts[0].split()[1])

    parts = parts[1].split()
    start = int(parts[0])-1
    end = int(parts[-1])-1

    return {
        "quantity": quantity,
        "start":start,
        "end":end
    }



def main():
    cargo_crane()

if __name__ == '__main__':
    main()
