import sys
input = sys.stdin.readline

def get_parent(parent, x):
    if parent[x] != x:
        parent[x] = get_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = get_parent(parent, a)
    b = get_parent(parent, b)
    if a != b:
        parent[a] = b

def find_parent(parent, a, b):
    return get_parent(parent, a) == get_parent(parent, b)

# 입력
n, m = map(int, input().split())
edges = []
for _ in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

parent = [i for i in range(n + 1)]
edges.sort()

result = 0
max_cost = 0

# 크루스칼 알고리즘
for cost, a, b in edges:
    if not find_parent(parent, a, b):
        union_parent(parent, a, b)
        result += cost
        max_cost = max(max_cost, cost)

print(result - max_cost)
