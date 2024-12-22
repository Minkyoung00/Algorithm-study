from collections import deque

N = int(input())
tri = [tuple(map(int, input().split())) for i in range(N)]

visit = [[0 for k in range(i)] for i in range(1,N+1)]
visit[0][0] = tri[0][0]

for i in range(1, N):
    for j in range(i+1):
        if j == 0:
            visit[i][j] = visit[i-1][j] + tri[i][j]
        elif j == i:
            visit[i][j] = visit[i-1][j-1] + tri[i][j] 
        else:
            visit[i][j] = max(visit[i-1][j], visit[i-1][j-1]) + tri[i][j]

print(max(visit[-1]))