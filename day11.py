#!/usr/local/bin/python3
'''
Advent of code day 11 - 2022
'''
import re
from collections import deque
from copy import deepcopy


def read_monkeys():
    "Read monkeys"
    monkeys = {}
    index = -1
    start = []
    with open('day11.txt', 'r', encoding="ascii") as file:
        while True:
            line = file.readline()
            if not line:
                break
            line = line.replace('\n', '')
            match = re.search(r'Monkey\s(\d+)', line)
            if match:
                index = int(match.group(1))
            match = re.search(r'Starting items:(.*)', line)
            if match:
                start = deque(map(int, match.group(1).split(',')))
                monkeys[index] = {'items': start}
            match = re.search(r'Operation: new = (.*)', line)
            if match:
                monkeys[index]['operation'] = match.group(1)
            match = re.search(r'Test: divisible by (\d+)', line)
            if match:
                monkeys[index]['div_by'] = int(match.group(1))
            match = re.search(r'If true: throw to monkey (\d+)', line)
            if match:
                monkeys[index]['if_true'] = int(match.group(1))
            match = re.search(r'If false: throw to monkey (\d+)', line)
            if match:
                monkeys[index]['if_false'] = int(match.group(1))
                assert len(monkeys[index]) == 5
    return monkeys


def monkey_business(_monkeys, iters, w_factor):
    "Simulate the monkeys and produce monkey business level"
    def _eval(operation, val):
        ops = operation.split()
        if ops[0] == ops[2] == 'old' and ops[1] == '*':
            return val * val
        if ops[1] == '+':
            return val + int(ops[2])
        return val * int(ops[2])

    n_monkeys = len(_monkeys)
    inspect = [0] * n_monkeys
    modulus = 1
    for index in range(n_monkeys):
        modulus *= _monkeys[index]['div_by']
    for _ in range(iters):
        for index in range(n_monkeys):
            while _monkeys[index]['items']:
                inspect[index] += 1
                val = _monkeys[index]['items'].popleft()
                worry = _eval(_monkeys[index]['operation'], val) // w_factor
                worry %= modulus
                if worry % _monkeys[index]['div_by'] == 0:
                    target = _monkeys[index]['if_true']
                else:
                    target = _monkeys[index]['if_false']
                _monkeys[target]['items'].append(worry)
    inspect.sort()
    return inspect[-1] * inspect[-2] if len(inspect) > 1 else -1


if __name__ == "__main__":
    M = read_monkeys()
    print('First solution:', monkey_business(deepcopy(M), 20, 3))
    print('Second solution:', monkey_business(deepcopy(M), 10000, 1))
