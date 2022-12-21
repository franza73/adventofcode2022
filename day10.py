#!/usr/local/bin/python3
'''
Advent of code day 10 - 2022
'''


def read_commands():
    "Read commands"
    _commands = []
    with open('day10.txt', 'r', encoding="ascii") as file:
        while True:
            line = file.readline()
            if not line:
                break
            line = line.replace('\n', '')
            _commands.append(line)
    return _commands


def decode(_commands):
    "Process the commands and decode the letters"
    time = 1
    val_x = 1
    res = '\n#'
    for cmd in _commands[:-1]:
        if cmd == 'noop':
            pass
        else:
            val = int(cmd.split()[1])
            res += '#' if time in set([val_x - 1, val_x, val_x + 1]) else '.'
            time += 1
            time %= 40
            if time == 0:
                res += '\n'
            val_x += val
        res += '#' if time in set([val_x - 1, val_x, val_x + 1]) else '.'
        time += 1
        time %= 40
        if time == 0:
            res += '\n'
    return res


def calculate_strength(_commands):
    "Process the commands and calculate strength"
    time = 1
    val_x = 1
    strength = 0
    for cmd in _commands:
        if cmd == 'noop':
            pass
        else:
            val = int(cmd.split()[1])
            time += 1
            if (time - 20) % 40 == 0:
                strength += time * val_x
            val_x += val
        time += 1
        if (time - 20) % 40 == 0:
            strength += time * val_x
    return strength


if __name__ == "__main__":
    CMDS = read_commands()
    print('First solution:', calculate_strength(CMDS))
    print('Second solution:', decode(CMDS).rstrip())
    # Visually: ECZUZALR
