import sys

filename = sys.argv[1]
with open(filename) as file:
    lines = file.readlines()
    size, graph = int(lines[0]), [list(map(int, x.split()[:-1])) for x in lines[1:]]
    graph.insert(0, [])

components = [[], ]
currently_component = 0
used = set()


def dfs(v):
    used.add(v)
    components[len(components) - 1].append(str(v))
    for sub_v in range(len(graph[v])):
        if graph[v][sub_v] not in used:
            dfs(graph[v][sub_v])


def find_components():
    global components
    for v in range(1, size + 1):
        if v not in used:
            dfs(v)
            components.append([])


find_components()
for component in components[:-1]:
    print(' '.join(component) + ' 0')
