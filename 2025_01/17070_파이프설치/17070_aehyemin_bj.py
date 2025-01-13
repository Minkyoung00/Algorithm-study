n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int ,input().split())))

dp = [[[0]*3 for _ in range(n)] for _ in range(n)]
dp[0][1][0] = 1
#0은 가로, (c, r+1) 확인

#1은 세로 (c+1, r) 학인 
#2는 대각선 (c+1, r+1) (c+1, r) (c, r+1) 확인

for r in range(n):
    for c in range(n):
        if graph[r][c] == 1:
            continue
        if c > 0 and graph[r][c] == 0:
            dp[r][c][0] += dp[r][c-1][0] + dp[r][c-1][2]
            
        if r > 0 and graph[r][c] == 0:
            dp[r][c][1] += dp[r-1][c][1] + dp[r-1][c][2]
           
        if c > 0 and r > 0 and graph[r][c] == 0 and graph[r-1][c] == 0 and graph[r][c-1] == 0:
            dp[r][c][2] += dp[r-1][c-1][2] + dp[r-1][c-1][1] + dp[r-1][c-1][0]
            
print(dp[n-1][n-1][0] + dp[n-1][n-1][1] + dp[n-1][n-1][2])
        
        