in_filename = 'in.txt'
out_filename = 'out.txt'


def write_file(_path, max_weight):
    with open('out.txt', 'w', encoding='utf-8') as file:
        if len(_path) is not 0:
            file.write("Y\n")
            result = ''
            for i in _path:
                result += str(i+1)+ " "
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
    matrix = [[-1 for _ in range(N)] for _ in range(N)]

    # for i in zip(range(1, len(weights) + 1), weights):

    for i in range(len(weights)):
        if len(weights[i]) > 0:
            for j in range(0, len(weights[i]), 2):
                matrix[weights[i][j] - 1][i] = weights[i][j + 1]
    return matrix


def apply_dijkstra(N, S, matrix):
    print(N, S, matrix)
    valid = [True] * N
    weight = [float('inf')] * N
    weight[S] = 0
    parent = [S] * (N)
    parent[S] = -1
    for i in range(N):
        min_weight = float('inf')
        ID_min_weight = -1
        # бирается мин метка вершины из не посещенных
        for i in range(N):
            if valid[i] and weight[i] < min_weight:
                min_weight = weight[i]
                ID_min_weight = i
        for i in range(N):
            if matrix[ID_min_weight][i] != -1:
                if weight[i] > max(weight[ID_min_weight], matrix[ID_min_weight][i]):
                    weight[i] = max(weight[ID_min_weight], matrix[ID_min_weight][i])
                    parent[i] = ID_min_weight
            valid[ID_min_weight] = False
    return weight, [x for x in parent]


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
    w, parents = apply_dijkstra(N, from_v - 1, matrix)
    path = find_path(from_v - 1, to_v - 1, parents)
    weight = sum([w[x] for x in path])
    if str(weight) == 'inf':
        write_file([], '')
    else:
        write_file(path, weight)


if __name__ == '__main__':
    main()
