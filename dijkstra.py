import heapq as hq

import math

in_filename = 'in.txt'
out_filename = 'out.txt'


def write_file(_path, max_weight):
    with open('out.txt', 'w', encoding='utf-8') as file:
        if len(_path) is not 0:
            file.write("Y\n")
            result = ''
            for i in _path:
                result += str(i + 1) + " "
            file.write(result.rstrip() + '\n')
            file.write(str(max_weight))
        else:
            file.write('N')


def read_file(filename):
    with open(filename) as file:
        lines = file.readlines()
        N, weights, to_v, from_v = lines[0], lines[1: -2], lines[-1], lines[-2]
        N, weights, from_v, to_v = int(N), [list(map(int, x.split()[:-1])) for x in weights], int(from_v), int(to_v)
        return N, weights, from_v, to_v


def transform_to_matrix(N, weights):
    matrix = [[] for _ in range(N)]
    print(weights)
    for i in range(len(weights)):
        if len(weights[i]) > 0:
            for j in range(0, len(weights[i]), 2):
                matrix[weights[i][j] - 1].append((i, weights[i][j + 1]))
    return matrix


def apply_dijkstra(G, s):
    n = len(G)
    visited = [False] * n
    weights = [math.inf] * n
    path = [-1] * n
    queue = []
    weights[s] = 1
    hq.heappush(queue, (1, s))
    while len(queue) > 0:
        g, u = hq.heappop(queue)
        visited[u] = True
        for v, w in G[u]:
            if not visited[v]:
                f = g * w
                if f < weights[v]:
                    weights[v] = f
                    path[v] = u
                    hq.heappush(queue, (f, v))
    return path, weights


def find_path(point_from, point_to, parents):
    path = []
    point_to = point_to
    if parents[point_to] < 1000000:
        path.append(point_to)
        v = point_to
        while v != point_from:
            w = parents[v]
            path.append(w)
            v = w
        path = path[::-1]
        return path
    return []


def main():
    N, weights, from_v, to_v = read_file(in_filename)
    matrix = transform_to_matrix(N, weights)
    print(matrix)
    parents, w = apply_dijkstra(matrix, from_v - 1)
    print(w, parents)
    if str(w[to_v - 1]) == 'inf':
        write_file([], '')
    else:
        path = find_path(from_v - 1, to_v - 1, parents)
        print(path)
        write_file(path, w[to_v - 1])




if __name__ == '__main__':
    main()
