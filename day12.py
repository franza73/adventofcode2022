#!/usr/local/bin/python3
'''
Advent of code day 12 - 2022
'''
from math import inf
from collections import defaultdict, deque


def read_graph():
    "Read graph"
    matrix = []
    with open('day12.txt', 'r', encoding="ascii") as file:
        while True:
            line = file.readline()
            if not line:
                break
            line = line.replace('\n', '')
            matrix += [list(line)]
    size_x, size_y = len(matrix), len(matrix[0])
    graph = defaultdict(list)
    for i in range(size_x):
        for j in range(size_y):
            if matrix[i][j] == 'S':
                begin = (i, j)
            elif matrix[i][j] == 'E':
                end = (i, j)
            for d_x, d_y in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                n_i, n_j = i + d_x, j + d_y
                if 0 <= n_i < size_x and 0 <= n_j < size_y:
                    if matrix[i][j] == 'S' and matrix[n_i][n_j] != 'a':
                        continue
                    if matrix[n_i][n_j] == 'E' and matrix[i][j] != 'z':
                        continue
                    if (matrix[i][j] != 'S' and matrix[n_i][n_j] != 'E' and
                       ord(matrix[n_i][n_j]) - ord(matrix[i][j]) > 1):
                        continue
                    graph[(n_i, n_j)] += [(i, j)]
    return graph, matrix, begin, end


# def best_path_dijkstra(graph, begin, end):
#     'Find length of best path between begin and end'
#     dist = {v: inf for v in graph}
#     dist[end] = inf
#     dist[begin] = 0
#     p_queue = []
#     visited = set()
#     heappush(p_queue, (0, begin))
#     while p_queue:
#         _, point = heappop(p_queue)
#         if point == end:
#             return dist[point]
#         if point in visited:
#             continue
#         visited.add(point)
#         for neigh in graph[point]:
#             if dist[point] + 1 < dist[neigh]:
#                 dist[neigh] = dist[point] + 1
#                 heappush(p_queue, (dist[neigh], neigh))
#     return -1


def best_path(graph, matrix, begin, end):
    'Find length of best path between begin and end'
    queue = deque([(0, end)])
    visited = set()
    first = second = inf
    while queue:
        depth, point = queue.popleft()
        if point == begin:
            if first == inf:
                first = depth
        if matrix[point[0]][point[1]] == 'a':
            if second == inf:
                second = depth
        if point in visited:
            continue
        visited.add(point)
        for neigh in graph[point]:
            queue += [(depth+1, neigh)]
    return first, second


if __name__ == "__main__":
    GRAPH, MATRIX, BEGIN, END = read_graph()
    F, S = best_path(GRAPH, MATRIX, BEGIN, END)
    print('First solution:', F)
    print('Second solution:', S)
