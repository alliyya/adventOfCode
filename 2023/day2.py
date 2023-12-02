#!/usr/bin/python3

def main():
    # part_1()
    part_2()


AVAILABLE_CUBES = {
    "red":12,
    "green":13,
    "blue":14
}

def clean_input(line, part_2=False):
    line = line.split(": ")[1]
    if part_2:
        line = line.replace(";", ",")
    return line

def reset_cube_counter():
    return  {
    "red":0,
    "green":0,
    "blue":0
    }
    
def count_cubes(cube_set):
    cube_counter = reset_cube_counter()
    cubes = cube_set.split(", ")
    for cube in cubes:
        cube_counter[cube.split(" ")[1]] += int(cube.split(" ")[0])
    return cube_counter

def row_check(line):
    cube_sets = line.split("; ")
    
    for cube_set in cube_sets:
        cube_counter = count_cubes(cube_set)
        if not compare_cubes(cube_counter):
            return False
    return True
    
    
def compare_cubes(cube_counter):
    for cube in cube_counter.keys():
        if cube_counter[cube] > AVAILABLE_CUBES[cube]:
            return False
    return True

def part_1():
    row = 1
    total = 0
    line = clean_input(input())
    total += row if row_check(line) else 0

    while line:
        try:
            row +=1
            line = clean_input(input())
            total += row if row_check(line) else 0
        except EOFError:
            break
    
    print(total)
    print(F"Sum of the IDs of those games: {total}")

def get_max_cubes(line):
    cubes = line.split(", ")
    max_cube = reset_cube_counter()
    
    for cube in cubes:
        count = int(cube.split(" ")[0])
        cube_color = cube.split(" ")[1]
        if count > max_cube[cube_color]:
            max_cube[cube_color] = count
    return max_cube 
        

def get_power(max_cube):
    return max_cube["red"] * max_cube["green"] * max_cube["blue"]


def part_2():
    total = 0
    line = clean_input(input(), True)

    total += get_power(get_max_cubes(line))
    
    while line:
        try:
            line = clean_input(input(), True)
            
            total += get_power(get_max_cubes(line))
        except EOFError:
            break
    
    print(total)
    print(F"Sum of the IDs of those games: {total}")


if __name__ == '__main__':
    main()
    
