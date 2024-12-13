from collections import deque

N = int(input())
tri = [tuple(map(int, input().split())) for i in range(N)]

visit = [[0 for k in range(i)] for i in range(1,N+1)]
visit[0][0] = tri[0][0]
result = []

for i in range(1, N):
    row = i
    for j in range(i+1):
        if j == 0:
            visit[row][j] = visit[row-1][j] + tri[row][j]
        elif j == i:
            visit[row][j] = visit[row-1][j-1] + tri[row][j] 
        else:
            visit[row][j] = max(visit[row-1][j], visit[row-1][j-1]) + tri[i][j]

print(max(visit[-1]))