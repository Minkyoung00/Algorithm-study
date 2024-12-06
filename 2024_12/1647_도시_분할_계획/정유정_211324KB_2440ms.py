import sys

vertex, edge = map(int, sys.stdin.readline().strip().split())
graph = []
parent = [0] * (vertex + 1)

for i in range(edge):
    graph.append(tuple(map(int, sys.stdin.readline().strip().split())))

for i in range(1, vertex):
    parent[i] = i
    
graph.sort(key=lambda x: x[2])


def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    root_a = find(a)
    root_b = find(b)

    if root_a < root_b:
        parent[root_b] = root_a
    else:
        parent[root_a] = root_b


result = 0
max_cost = 0
for g in graph:
    a, b, cost = g
    if find(a) != find(b):
        union(a, b)
        result += cost
        if cost > max_cost:
            max_cost = cost

print(result - max_cost)

