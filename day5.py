#!/usr/local/bin/python3
'''
Advent of code day 5 - 2022
'''
from collections import defaultdict, deque
import re
from copy import deepcopy


def decodeCrateMover9000(L, M):
    for count, origin, dest in M:
        for _ in range(count):
            L[dest].append(L[origin].pop())
    return ''.join(L[k][-1] for k in sorted(L.keys()))


def decodeCrateMover9001(L, M):
    for count, origin, dest in M:
        moves = []
        for _ in range(count):
            moves += [L[origin].pop()]
        moves.reverse()
        for m in moves:
            L[dest].append(m)
    return ''.join(L[k][-1] for k in sorted(L.keys()))


if __name__ == "__main__":
    L = defaultdict(deque)
    M = []
    MODE = 1
    RE = r'move (\d+) from (\d+) to (\d+)'
    with open('day5.txt', 'r', encoding="ascii") as f:
        while True:
            line = f.readline()
            if not line:
                break
            line = re.sub(r'[\n\r]+', '', line)
            if line == '':
                MODE = 2
                continue
            if MODE == 1:
                for i, ni in enumerate(list(line)):
                    if re.search(r'[A-Z]', ni):
                        key = 1 + (i-1) // 4
                        L[key].appendleft(ni)
            else:
                M.append(tuple(map(int, re.search(RE, line).groups())))

    print('First solution:', decodeCrateMover9000(deepcopy(L), M))
    print('Second solution:', decodeCrateMover9001(deepcopy(L), M))
