#!/usr/local/bin/python3
'''
Advent of code day 2 - 2022
'''


RESULT = {'AX': 1+3, 'AY': 2+6, 'AZ': 3+0,
          'BX': 1+0, 'BY': 2+3, 'BZ': 3+6,
          'CX': 1+6, 'CY': 2+0, 'CZ': 3+3}

MODIFIED = {'AX': 3+0, 'AY': 1+3, 'AZ': 2+6,
            'BX': 1+0, 'BY': 2+3, 'BZ': 3+6,
            'CX': 2+0, 'CY': 3+3, 'CZ': 1+6}

score = 0
score2 = 0
with open('day2.txt', 'r', encoding="ascii") as f:
    while True:
        line = f.readline()
        if not line:
            break
        a, b = line.strip().split()
        score += RESULT[a+b]
        score2 += MODIFIED[a+b]
print('First solution:', score)
print('Second solution:', score2)
