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


def get_horizontal_coord(x1, y1,x2,y2):
    coord = []
    if x2 > x1:
        num = x1
        while num != x2:
            coord.append([num, y1])
            print( num, y1)
            num +=1

    elif x1 > x2:
        num = x2
        while num != x1:
            coord.append([num, y1])
            print( num, y1)
            num +=1

    print(coord)


def get_coordinates(line,diagonal=False):
    path = line.split(" -> ")
    print(path)
    x1,y1 = path[0].split(",")
    x2,y2 = path[1].split(",")
    x1 = int(x1)
    y1 = int(y1)
    x2 = int(x2)
    y1 = int(y1)
    
    print(x1, y1)
    print(x2, y2)
    print("--")
    coord = []
    get_horizontal_coord(x1, y1,x2, y2)



def main():
    lines = []
    # lines = input("Lines of vents:") #.split(",")
    # boards = []

    while True:
        try:
            lines.append( input())
            # boards.append(read_board())
        except EOFError:
            break

    print(lines)
    get_coordinates(lines[0])
    # part_1(boards, numbers)
    # part_2(boards, numbers)


if __name__ == '__main__':

    main()
