#!/usr/bin/python3
import re
def main():
    # part_1()
    part_2()

def removeLetters(line):
    return re.sub('[a-zA-Z]', '', line)

NUMBERS = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

def findNumbers(line):
    for key in NUMBERS.keys():
        if key in line:
            line = line.replace(key, F"{key}{NUMBERS[key]}{key}")

    return removeLetters(line)     

def calibrate(line): 
    return int(line[0]+line[-1])

def part_2():
    line = input()
    total = calibrate(findNumbers(line))
    while line:
        try:
            line = input()
            total += calibrate(findNumbers(line))
        except EOFError:
            break
    print(F"Sum of all Callibration values: {total}")

    
def part_1():
    line = calibrate(removeLetters(input()))
    total = line
    
    while line:
        try:
            line = calibrate(removeLetters(input()))
            total += line

        except EOFError:
            break
    print(F"Sum of all Callibration values: {total}")


if __name__ == '__main__':
    main()
    
