#!/usr/local/bin/python3
'''
Advent of code day 13 - 2022
'''
from functools import cmp_to_key


def read_pairs():
    "Read input"
    pairs = []
    with open('day13.txt', 'r', encoding="ascii") as file:
        while True:
            line = file.readline()
            if not line:
                break
            line = line.replace('\n', '')
            if len(line) == 0:
                continue
            pairs += [eval(line)]
    return pairs


def cmp(par1, par2):
    "Compare the lists. Also used as sort comparison function"
    if isinstance(par1, list) and isinstance(par2, list):
        for a_i, b_i in zip(par1, par2):
            val = cmp(a_i, b_i)
            if val != 0:
                return val
        res = 0
        if len(par1) > len(par2):
            res = -1
        elif len(par1) < len(par2):
            res = 1
        return res
    if isinstance(par1, int) and isinstance(par2, list):
        return cmp([par1], par2)
    if isinstance(par1, list) and isinstance(par2, int):
        return cmp(par1, [par2])
    res = 0
    if par1 > par2:
        res = -1
    elif par1 < par2:
        res = 1
    return res


def count_packets_in_right_order(pairs):
    "Count how many pairs of packets are in the correct order"
    i = 0
    cnt = 0
    for i in range(len(pairs) // 2):
        if cmp(pairs[2*i], pairs[2*i+1]) >= 0:
            cnt += i + 1
    return cnt


def find_decoder_key(pairs):
    "Sort packets and find the decoder key"
    v_1, v_2 = [[2]], [[6]]
    result = 1
    pairs.extend([v_1, v_2])
    for i, a_i in enumerate(sorted(pairs, key=cmp_to_key(cmp), reverse=True)):
        if a_i in (v_1, v_2):
            result *= i+1
    return result


def main():
    "main function"
    pairs = read_pairs()
    print('First solution:', count_packets_in_right_order(pairs))
    print('Second solution:', find_decoder_key(pairs))


if __name__ == "__main__":
    main()
