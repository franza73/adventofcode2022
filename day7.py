#!/usr/local/bin/python3
'''
Advent of code day 7 - 2022
'''
import re
from collections import defaultdict
from math import inf


def calculate_dir_sizes():
    def _explore(dir):
        sum = 0
        for n in files[dir]:
            if type(n) == int:
                sum += n
            else:
                sum += _explore(dir + '/' + n)
        dir_sizes[dir] = sum
        return sum
    dir_sizes = {}
    _explore('')
    return dir_sizes


def total_size(dir_sizes):
    SIZE = 100000
    cnt = 0
    for v in dir_sizes.values():
        if v < SIZE:
            cnt += v
    return cnt


def get_size_to_delete(dir_sizes):
    DISK_AVAILABLE = 70000000
    MIN_UNUSED = 30000000
    total_used = dir_sizes['']
    unused_space = DISK_AVAILABLE - total_used
    need_to_delete = MIN_UNUSED - unused_space
    size_to_delete = inf
    for size in dir_sizes.values():
        if size_to_delete == -1 or need_to_delete <= size:
            size_to_delete = min(size_to_delete, size)
    return size_to_delete


if __name__ == "__main__":
    pwd = []
    files = defaultdict(list)
    with open('day7.txt', 'r', encoding="ascii") as f:
        while True:
            line = f.readline()
            if not line:
                break
            line = line.replace('\n', '')
            m = re.search(r'\$ cd (\S+)', line)
            if m:
                dir_name = m.group(1)
                if dir_name == '..':
                    pwd.pop()
                elif dir_name == '/':
                    pwd += ['']
                else:
                    pwd += [dir_name]
            elif line != '$ ls':
                a, b = line.split()
                KEY = '/'.join(pwd)
                if a != 'dir':
                    files[KEY] += [int(a)]
                else:
                    files[KEY] += [b]

    dir_sizes = calculate_dir_sizes()
    print('First solution:', total_size(dir_sizes))
    print('Second solution:', get_size_to_delete(dir_sizes))
