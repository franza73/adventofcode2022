#!/usr/local/bin/python3
'''
Advent of code day 7 - 2022
'''
import re
from collections import defaultdict
import math


def calculate_dir_sizes():
    def _explore(_dir):
        _sum = 0
        for name in files[_dir]:
            if isinstance(name, int):
                _sum += name
            else:
                _sum += _explore(_dir + '/' + name)
        _dir_sizes[_dir] = _sum
        return _sum
    _dir_sizes = {}
    _explore('')
    return _dir_sizes


def total_size(_dir_sizes):
    max_size = 100000
    cnt = 0
    for size in _dir_sizes.values():
        if size < max_size:
            cnt += size
    return cnt


def get_size_to_delete(_dir_sizes):
    disk_unavailable = 70000000
    min_unused = 30000000
    total_used = _dir_sizes['']
    unused_space = disk_unavailable - total_used
    need_to_delete = min_unused - unused_space
    size_to_delete = math.inf
    for size in _dir_sizes.values():
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
