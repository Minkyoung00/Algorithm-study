N = int(input())
M = int(input())
edges = [tuple(map(int, input().split())) for i in range(M)]
parent = [i for i in range(N+1)]

edges.sort(key = lambda x: x[2])
total_cost = 0

def find(vertex):
    if parent[vertex] != vertex:
        parent[vertex] = find(parent[vertex])
    return parent[vertex]

def union(ver1, ver2, cost):
    global total_cost
    parent[find(ver2)] = ver1
    total_cost += cost

for edge in edges:
    a, b, c = edge
    if find(a) != find(b):
        union(a,b,c)

print(total_cost)
    