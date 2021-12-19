import math
"""
https://adventofcode.com/2015/day/1
Usage:
    cat day4_input.txt | python3 day4.py
        > The steps are: xxx

    ou
    python3 day4.py
        input numbers and ctrl-d (EOF) to end inputs
        > The steps are: xxx
"""


def part_1(boards, numbers):
    for x in numbers:
        for y in range(len(boards)):
            boards[y] = update_board(boards[y], x)
            if check_rows(boards[y]) or check_cols(boards[y]):
                print(F"The first winning board is #{y+1}")
                print(F"The final score is: {int(x)*get_board_sum(boards[y])}")
                return


def part_2(boards, numbers):
    unwon_boards = [x for x in range(len(boards))]
    for x in numbers:
        for y in range(len(boards)):
            boards[y] = update_board(boards[y], x)
            if check_rows(boards[y]) or check_cols(boards[y]):
                if y in unwon_boards:
                    unwon_boards.remove(y)
                    if len(unwon_boards) == 0:
                        print(F"The last board to win is #{y+1}")
                        print(
                            F"The final score is: {int(x)*get_board_sum(boards[y])}")
                        return


def read_board():
    board = []
    for _ in range(5):
        line = [x for x in input().split(" ") if x]
        board += line
    return board


def update_board(board, num):
    if num in board:
        board[board.index(num)] = "X"
    return board


def print_board(board):
    for x in range(5):
        for y in board[x*5:(x*5)+5]:
            print(f'{y:>3s}', end="")
        print()


def check_rows(board):
    for x in range(5):
        if board[x*5:(x*5)+5].count('X') == 5:
            return True
    return False


def check_cols(board):
    for x in range(5):
        if board[x::5].count('X') == 5:
            return True
    return False


def get_board_sum(board):
    sum = 0
    for x in board:
        if x != "X":
            sum += int(x)

    return sum


def main():
    numbers = input("The numbers drawn is:").split(",")
    boards = []

    while True:
        try:
            input()
            boards.append(read_board())
        except EOFError:
            break

    part_1(boards, numbers)
    part_2(boards, numbers)


if __name__ == '__main__':

    main()
