#!/usr/bin/python3
"""
https://adventofcode.com/2019/day/3
Usage:
cat day3_input.txt |  python3 day3.py

"""
directions = {
    "R": (1, 0),
    "L": (-1, 0),
    "U": (0, 1),
    "D": (0, -1)
}
initial_pos = (1, 1)


def add(pt1, pt2):
    return (pt1[0] + pt2[0], pt1[1] + pt2[1])


def sub(pt1, pt2):
    return (pt1[0] - pt2[0], pt1[1] - pt2[1])


def get_points(line):
    steps = line.split(",")
    points = []
    current = initial_pos

    for x in steps:
        direction = x[0]
        size = int(x[1:])
        for x in range(0, size):
            current = add(current, directions[direction])
            points.append(current)

    return(points)


def closest_intersection(point, points):
    distances = []
    for x in points:
        temp = sub(x, point)
        dist = abs(temp[0]) + abs(temp[1])
        distances.append(dist)

    return(min(distances))


def get_min_steps(points, path1, path2):
    steps = []
    for x in points:
        num1 = path1.index(x)
        num2 = path2.index(x)
        steps.append(num1 + num2 + 2)

    return(min(steps))


def main():
    line1 = input()
    line2 = input()

    path1 = get_points(line1)
    path2 = get_points(line2)

    intersections = list(set(path1).intersection(set(path2)))

    # part 1
    min_dist = closest_intersection(initial_pos, intersections)
    print("Part 1 result:", min_dist)

    # part 2
    min_steps = get_min_steps(intersections, path1, path2)
    print("Part 2 result:", min_steps)


if __name__ == '__main__':
    main()
