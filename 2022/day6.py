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


def process_packet(buffer, marker_size):
    substring = []
    for index, char in enumerate(buffer):

        substring.append(char)
        if (len(substring)>marker_size):
            substring.pop(0)
            marker = set(substring)
            if len(marker) == marker_size:
               return(index + 1)
               break


def main():
    datastream_buffer = input()
    print(F"Part 1: {process_packet(datastream_buffer,4)} ")
    print(F"Part 2: {process_packet(datastream_buffer,14)} ")


if __name__ == '__main__':
    main()
