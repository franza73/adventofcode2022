#!/usr/local/bin/python3
'''
Advent of code day 14 - 2022
'''
from math import inf


def read_input():
    "Read input"
    x_min, x_max, y_min, y_max = inf, 0, 0, 0
    wall = set()
    with open('day14.txt', 'r', encoding="ascii") as file:
        while True:
            line = file.readline()
            if not line:
                break
            line = line.rstrip()
            wall_i = list(map(lambda x: tuple(map(int, x.split(','))),
                          line.split(' -> ')))
            for i in range(1, len(wall_i)):
                if wall_i[i][0] == wall_i[i-1][0]:
                    pt1, pt2 = sorted([wall_i[i][1], wall_i[i-1][1]])
                    for j in range(pt1, pt2 + 1):
                        wall.add((wall_i[i][0], j))
                else:
                    pt1, pt2 = sorted([wall_i[i][0], wall_i[i-1][0]])
                    for k in range(pt1, pt2 + 1):
                        wall.add((k, wall_i[i][1]))
            for x_i, y_i in wall_i:
                x_min = min(x_min, x_i)
                x_max = max(x_max, x_i)
                y_max = max(y_max, y_i)
    return wall, (x_min, x_max, y_min, y_max)


def simulate(maze, limits, floor=False):
    "Simulate dropping sand until it spills out of the structure"
    def next_position(pos):
        res = [(pos[0], pos[1]+1),
               (pos[0]-1, pos[1]+1),
               (pos[0]+1, pos[1]+1)]
        for res_i in res:
            if res_i not in maze:
                return res_i
        return None

    x_min, x_max, _, y_max = limits
    if floor:
        for x_i in range(x_min - 200, x_max + 200):
            maze.add((x_i, y_max+2))
    k = 0
    while True:
        pos = (500, 0)
        while True:
            new = next_position(pos)
            if not new:
                maze.add(pos)
                break
            pos = new
            if not floor and (pos[0] < x_min or pos[0] > x_max):
                return k
        k += 1
        if pos[1] == 0:
            return k


def main():
    "main function"
    maze, limits = read_input()
    print('First solution:', simulate(set(maze), limits))
    print('Second solution:', simulate(set(maze), limits, floor=True))


if __name__ == "__main__":
    main()
