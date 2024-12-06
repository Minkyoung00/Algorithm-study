import sys
input = sys.stdin.readline

def find(parent, edge):
    if parent[edge] != edge:
        parent[edge] = find(parent, parent[edge])
    return parent[edge]

N, M = map(int, input().split())
roads = [tuple(map(int, input().split())) for i in range(M)]

roads.sort(key=lambda road: road[2])

parent = [i for i in range(N+1)]
cost, max_cost = 0, 0

rank = [0] * (N+1)

for road in roads:
    A, B, C = road

    root_A = find(parent, A)
    root_B = find(parent, B)
    if root_A != root_B:
        cost += C
        max_cost = C

        if rank[root_A] > rank[root_B]:
            parent[root_B] = root_A

        elif rank[root_A] < rank[root_B]:
            parent[root_A] = root_B

        else:
            parent[root_A] = root_B
            rank[root_B] += 1
   
print(cost - max_cost)