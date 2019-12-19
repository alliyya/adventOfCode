#!/usr/bin/python3

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

    return(set(points))


def closest_intersection(point, points):
    distances = []
    for x in points:
        temp = sub(x, point)
        dist = abs(temp[0]) + abs(temp[1])
        distances.append(dist)

    return(min(distances))


def main():
    line1 = input()
    line2 = input()

    path1 = get_points(line1)
    path2 = get_points(line2)

    intersections = path1.intersection(path2)
    min_dist = closest_intersection(initial_pos, intersections)
    print(min_dist)


if __name__ == '__main__':
    main()
