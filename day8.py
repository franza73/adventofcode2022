#!/usr/local/bin/python3
'''
Advent of code day 8 - 2022
'''
from collections import defaultdict


def read_matrix():
    "Read square matrix of integers"
    matrix = []
    with open('day8.txt', 'r', encoding="ascii") as file:
        while True:
            line = file.readline()
            if not line:
                break
            line = line.replace('\n', '')
            matrix += [[int(li) for li in line]]
    size_x, size_y = len(matrix), len(matrix[0])
    assert size_x == size_y
    return matrix, size_x


def count_visible_trees(matrix, size):
    "Count visible trees"
    visible = defaultdict(int)
    for i in range(size):
        level_lr = -1
        level_rl = -1
        level_ud = -1
        level_du = -1
        for j in range(size):
            if matrix[i][j] > level_lr:
                visible[(i, j)] += 1
                level_lr = matrix[i][j]
            if matrix[i][size-1-j] > level_rl:
                visible[(i, size-1-j)] += 1
                level_rl = matrix[i][size-1-j]
            if matrix[j][i] > level_ud:
                visible[(j, i)] += 1
                level_ud = matrix[j][i]
            if matrix[size-1-j][i] > level_du:
                visible[(size-1-j, i)] += 1
                level_du = matrix[size-1-j][i]
    return len(visible)


def highest_scenic_score(matrix, size):
    "Calculates the scenic score"
    best = 0
    for i in range(1, size-1):
        for j in range(1, size-1):
            down = up = right = left = 1
            while i+down < size-1 and matrix[i+down][j] < matrix[i][j]:
                down += 1
            while 0 < i-up and matrix[i-up][j] < matrix[i][j]:
                up += 1
            while j+right < size - 1 and matrix[i][j+right] < matrix[i][j]:
                right += 1
            while 0 < j-left and matrix[i][j-left] < matrix[i][j]:
                left += 1
            product = up * down * left * right
            best = max(best, product)
    return best


if __name__ == "__main__":
    M, N = read_matrix()
    print('First solution:', count_visible_trees(M, N))
    print('Second solution:', highest_scenic_score(M, N))
