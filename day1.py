#!/usr/local/bin/python3
'''
Advent of code day 1 - 2022
'''


s = [0]
with open('day1.txt', 'r', encoding="ascii") as f:
    while True:
        line = f.readline()
        if not line:
            break
        number = line.strip()
        if number:
            s[-1] += int(number)
        else:
            s += [0]
print('First solution:', max(s))
print('Second solution:', sum(sorted(s)[-3:]))
