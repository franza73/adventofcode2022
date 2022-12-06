#!/usr/local/bin/python3
'''
Advent of code day 6 - 2022
'''


if __name__ == "__main__":
    index0 = -1
    index1 = -1
    with open('day6.txt', 'r', encoding="ascii") as f:
        line = f.readline()
        L = len(line)
        for i in range(L):
            if index0 == -1 and i >= 4 and len(set(line[i-4:i])) == 4:
                index0 = i
            if index1 == -1 and i >= 14 and len(set(line[i-14:i])) == 14:
                index1 = i
    print('First solution:', index0)
    print('Second solution:', index1)
