#!/usr/local/bin/python3
'''
Advent of code day 9 - 2022
'''
DIRS = {'U': (0, -1), 'D': (0, 1), 'L': (-1, 0), 'R': (1, 0)}


def read_moves():
    "Read moves for the head"
    _moves = []
    with open('day9.txt', 'r', encoding="ascii") as file:
        while True:
            line = file.readline()
            if not line:
                break
            line = line.replace('\n', '')
            _moves.append(line.split())
    return _moves


def count_last_tail_positions(_moves, tail_size=1):
    "Count positions for a tail with specified number of links"
    head = (0, 0)
    tail = [(0, 0)] * tail_size
    visited = set()
    for pos, val in _moves:
        for _ in range(int(val)):
            head = (head[0]+DIRS[pos][0], head[1]+DIRS[pos][1])
            _head = list(head)
            for i in range(tail_size):
                d_x = abs(tail[i][0] - _head[0])
                d_y = abs(tail[i][1] - _head[1])
                if d_x == 2 and d_y == 2:
                    tail[i] = ((tail[i][0] + _head[0]) // 2,
                               (tail[i][1] + _head[1]) // 2)
                elif d_x == 2:
                    tail[i] = ((tail[i][0] + _head[0]) // 2, _head[1])
                    assert d_y < 2
                elif d_y == 2:
                    tail[i] = (_head[0], (tail[i][1] + _head[1]) // 2)
                    assert d_x < 2
                _head = tail[i]
            visited.add(tail[-1])
    return len(visited)


if __name__ == "__main__":
    M = read_moves()
    print('First solution:', count_last_tail_positions(M))
    print('Second solution:', count_last_tail_positions(M, 9))
