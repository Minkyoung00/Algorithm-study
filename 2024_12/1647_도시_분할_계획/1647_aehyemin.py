import sys
input = sys.stdin.readline
def find(n):
    if parent[n] != n:
        parent[n] = find(parent[n])
    return parent[n]

def union(a,b):
    a = find(a)
    b = find(b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


N, M = map(int, input().split())
graph = []
parent = list(range(N+1))
for _ in range(M):
    A, B, C = map(int, input().split())
    graph.append((A, B, C))
graph.sort(key=lambda x:x[2])
ans = 0
end = 0

for A,B,C in graph:
    if find(A) != find(B):
        union(A,B)
        ans += C
        end = C
print(ans - end)
        