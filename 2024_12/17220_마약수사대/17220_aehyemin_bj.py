from collections import deque
N, M = map(int, input().split()) #N은 노드 수, M은 간선 수
adj = [[] for _ in range(N)] #인접 리스트
ind = [0] * N
for _ in range(M):
    A, B = input().split()
    A, B = ord(A)-65, ord(B)-65
    adj[A].append(B)
    ind[B] += 1
    
data = input().split()
K = int(data[0])
caught = {ord(x)-65 for x in data[1:]}
origins = [i for i in range(N) if ind[i]==0 and i not in caught]

vis = set(origins)
q = deque(origins)
while q:
    c = q.popleft()
    for nx in adj[c]:
        if nx not in caught and nx not in vis:
            vis.add(nx)
            q.append(nx)

print(sum(1 for i in vis if i not in caught and ind[i]>0))