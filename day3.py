#!/usr/local/bin/python3
'''
Advent of code day 3 - 2022
'''


def priority(c):
    if 'a' <= c <= 'z':
        return ord(c) - ord('a') + 1
    elif 'A' <= c <= 'Z':
        return ord(c) - ord('A') + 27


score1 = 0
score2 = 0
i = 0
with open('day3.txt', 'r', encoding="ascii") as f:
    while True:
        line = f.readline()
        if not line:
            break
        line = line.strip()
        L = len(line)
        # -- score 1 --
        a, b = line[:L//2], line[L//2:]
        common = set(a).intersection(set(b))
        score1 += priority(common.pop())
        # -- score 2 --
        if i % 3 == 0:
            v = set(line)
        else:
            v = v.intersection(set(line))
        if i % 3 == 2:
            score2 += priority(v.pop())

        i += 1

print('First solution:', score1)
print('Second solution:', score2)
