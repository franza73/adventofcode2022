#!/usr/local/bin/python3
'''
Advent of code day 4 - 2022
'''
import re


contains = 0
overlaps = 0
with open('day4.txt', 'r', encoding="ascii") as f:
    while True:
        line = f.readline()
        if not line:
            break
        line = line.strip()
        a, b, c, d = map(int, re.split(r'[-,]', line))
        if (a >= c and b <= d) or (a <= c and b >= d):
            contains += 1
        if a <= c <= b or c <= a <= d:
            overlaps += 1
print('First solution:', contains)
print('Second solution:', overlaps)
