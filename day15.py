#!/usr/local/bin/python3
'''
Advent of code day 15 - 2022
'''
import re


def read_input():
    "Read input"
    res = []
    expr = r'.*x=(-?\d+), y=(-?\d+).*x=(-?\d+), y=(-?\d+)'
    with open('day15a.txt', 'r', encoding="ascii") as file:
        while True:
            line = file.readline()
            if not line:
                break
            res += [[int(val) for val in re.search(expr, line).groups(1)]]
    return res


def n_positions_with_no_beacon(points, line):
    "Count positions with no beacon for a line specified"
    lst = []
    beacon_in_line = set()
    for point in points:
        sensor, beacon = point[0:2], point[2:4]
        if beacon[1] == line:
            beacon_in_line.add(tuple(beacon))
        d_sl = abs(sensor[1] - line)
        d_sb = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
        if d_sl <= d_sb:
            delta = d_sb - d_sl
            lst += [[sensor[0]-delta, sensor[0]+delta]]
    lst.sort()
    assert len(lst) > 0
    res = []
    for lst_i in lst:
        if res and lst_i[0] <= res[-1][1]:
            res[-1][1] = max(res[-1][1], lst_i[1])
        else:
            res += [lst_i]
    d_res = 0
    for pt1, pt2 in res:
        d_res += pt2 - pt1 + 1
    return d_res - len(beacon_in_line)


def calculate_tuning_frequency(points):
    "Find tuning frequency"
    def dist(pt1, pt2):
        return abs(pt1[0] - pt2[0]) + abs(pt1[1] - pt2[1])

    points.sort()
    for point in points:
        sensor, beacon = point[0:2], point[2:4]
        print(sensor, dist(sensor, beacon))

    # from two centers + radius, find points that
    # have dist == d1 + 1 AND dist == d2 + 1 from
    # S1 and S2.
    return 'TODO'


def main():
    "main function"
    points = read_input()
    # print('First solution:', n_positions_with_no_beacon(points, 2000000))
    print('Second solution:', calculate_tuning_frequency(points))


if __name__ == "__main__":
    main()
