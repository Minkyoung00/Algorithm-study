import sys
input = sys.stdin.readline

N, M = map(int, input().split())

edge = []
for _ in range(M):
	A, B, C = map(int, input().split())
	edge.append([A, B, C])

parent = []

for v in range(N+1):
    parent.append(v)

edge.sort(key=lambda e: e[2])

def find(v):
    if v != parent[v]:
        parent[v] = find(parent[v])
    return parent[v]

cost = []
for e in edge:
	u, v, w = e

	# u의 head 랑 v의 head 비교
	if find(u) != find(v):
		if find(u) < find(v):
			parent[find(v)] = find(u) #v
		else:
			parent[find(u)] = find(v) #u
		cost.append(w)

print(sum(cost) - max(cost))