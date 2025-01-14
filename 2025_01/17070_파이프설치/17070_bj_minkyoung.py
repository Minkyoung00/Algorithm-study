N = int(input())
room = [list(map(int, input().split())) for i in range(N)]

dp = [[(0,0,0)] * (N+1) for i in range(N+1)]

dp[1][2] = (1, 0, 0) if room[0][1] == 0 else (0, 0, 0)  # (가로, 세로, 대각선)

for i in range(3, N+1):
    dp[1][i] = dp[1][i-1] if room[0][i-1] == 0 else (0,0,0)

for r in range(2, N+1):
    for c in range(1, N+1):
        if room[r-1][c-1]:
            dp[r][c] = (0,0,0)
        else:
            if not room[r-2][c-1] and not room[r-1][c-2]:
                dp[r][c] = (sum(dp[r][c-1]) - dp[r][c-1][1], sum(dp[r-1][c]) - dp[r-1][c][0], sum(dp[r-1][c-1]))
            else:
                dp[r][c] = (sum(dp[r][c-1]) - dp[r][c-1][1], sum(dp[r-1][c]) - dp[r-1][c][0], 0)

print(sum(dp[-1][-1]))

