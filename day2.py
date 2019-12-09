"""
Usage:
cat day2_input.txt |  python3 day2.py 

"""


def main():
    string = input()
    numbers = [int(x) for x in string.split(",")]
    index = 0
    print("Initial Numbers:", *numbers, sep=" ")

    # before running the program, replace position 1 with the value 12 and replace position 2 with the value 2
    numbers[1] = 12
    numbers[2] = 2
    print("Initial Numbers:", *numbers, sep=" ")

    while index < len(numbers):
        # getting output value
        output = 0
        if numbers[index] == 1:
            output = numbers[numbers[index + 1]] + numbers[numbers[index + 2]]
        elif numbers[index] == 2:
            output = numbers[numbers[index + 1]] * numbers[numbers[index + 2]]
        elif numbers[index] == 99:
            break
        else:
            print("Unexpected Value")
            break

        numbers[numbers[index + 3]] = output
        index += 4

    print("Final Numbers:", *numbers, sep=" ")


if __name__ == '__main__':
    main()
