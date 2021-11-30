"""
https://adventofcode.com/2019/day/2
Usage:
cat day2_input.txt |  python3 day2.py

"""
import copy


def get_updated_numbers(numbers):
    index = 0
    while index < len(numbers):
        # getting output value
        output = 0
        try:
            if numbers[index] == 1:
                output = numbers[numbers[index + 1]] + numbers[numbers[index + 2]]
            elif numbers[index] == 2:
                output = numbers[numbers[index + 1]] * numbers[numbers[index + 2]]
            elif numbers[index] == 99:
                break
            else:
                print("Unexpected Value")
                break
        except IndexError as e:
            print("\n!Invalid indexes provided: ", numbers[index: index + 3])
            print("!Max list index:", len(numbers))
            print()

        numbers[numbers[index + 3]] = output
        index += 4
    return numbers


def find_inital_num(og_numbers):
    # Naive approach --> could use itertools.product
    # --> for noun, verb in product(range(0, 100), range(0, 100)):

    # Each of the two input values(noun,verb) will be between 0 and 99,
    for noun in range(0, 100):
        for verb in range(0, 100):
            numbers = copy.deepcopy(og_numbers)
            numbers[1] = noun
            numbers[2] = verb
            numbers = get_updated_numbers(numbers)
            if numbers[0] == 19690720:
                return numbers
    return og_numbers


def part_2(numbers):
    return find_inital_num(numbers)


def part_1(numbers):
    numbers[1] = 12
    numbers[2] = 2
    return get_updated_numbers(numbers)


def main():
    string = input()
    og_numbers = [int(x) for x in string.split(",")]

    print("Initial Numbers:", *og_numbers, sep=" ")

    # numbers = part_1(og_numbers)
    numbers = part_2(og_numbers)

    print("Final Numbers:", *numbers, sep=" ")
    noun = numbers[1]
    verb = numbers[2]
    print("\n100 * noun + verb = ?")
    print("100 *", noun, "+", verb, " = ", (100 * noun) + verb)

if __name__ == '__main__':
    main()
