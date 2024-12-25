def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]
# parent [x] != x 면 자기가 루트 노드

def union(a,b):
    a = find(a)
    b = find(b)
    if a < b :
        parent[a] = b
    else:
        parent[b] = a

n = int(input())
m = int(input())

edges = []

for _ in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))
parent = [i for i in range(n+1)]

edges.sort()
result = 0

for edge in edges:
    cost, a, b = edge
    if find(a) != find(b):
        union(a, b)
        result += cost
print(result)