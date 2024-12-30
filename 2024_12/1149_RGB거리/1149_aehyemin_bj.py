n = int(input())
dp = [0] * n
for i in range(n):
    dp[i] = list(map(int, input().split()))
# 1번 집의 색은 2번 집의 색과 같지 않아야 한다.
# N번 집의 색은 N-1번 집의 색과 같지 않아야 한다.
# i(2 ≤ i ≤ N-1)번 집의 색은 i-1번, i+1번 집의 색과 같지 않아야 한다.

for k in range(1, n):
    dp[k][0] = min(dp[k-1][1], dp[k-1][2]) + dp[k][0]
    dp[k][1] = min(dp[k-1][2], dp[k-1][0]) + dp[k][1]
    dp[k][2] = min(dp[k-1][0], dp[k-1][1]) + dp[k][2]
print(min(dp[n-1]))