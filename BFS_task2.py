from collections import deque

filename = "in.txt"


def bfs():
    queue = deque()
    visited = set()
    parents = [0 for _ in range(size + 1)]
    parents[1] = -1
    queue.append(1)
    visited.add(1)
    while len(queue) > 0:
        v = queue.popleft()
        print(v)
        for w in range(1, size + 1):
            if graph[v][w] != 0:
                print('--', w)
                if w not in visited:
                    visited.add(w)
                    queue.append(w)
                    parents[w] = v
                elif parents[v] != w:
                    cycle = set()
                    next_v = w
                    while next_v != -1:
                        cycle.add(next_v)
                        next_v = parents[next_v]
                    next_v = v
                    while next_v != -1:
                        cycle.add(next_v)
                        next_v = parents[next_v]
                    return 'N', sorted(list(cycle))
    return 'A'


def add_rubbish_at_0(array):
    array.insert(0, -1)
    return array


with open(filename) as file:
    lines = file.readlines()
    size, graph = int(lines[0]), [list(map(int, add_rubbish_at_0(x.split()))) for x in lines[1:]]
    graph.insert(0, [])

a = bfs()
print(a)
res = ''
res += a[0]
if len(a) == 2:
    res += " "
    for i in a[1]:
        res += str(i) + " "

res = res[:-1]
with open('out.txt', mode='w') as file:
    file.write(res)
