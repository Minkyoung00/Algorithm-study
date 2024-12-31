K = int(input())
arr = [list(map(int, input().split())) for _ in range(K)]

dp = [[0]*3 for _ in range(K)]

dp[0][0] = arr[0][0]
dp[0][1] = arr[0][1]
dp[0][2] = arr[0][2]

for i in range(1, K):
    dp[i][0] = arr[i][0]+min(dp[i-1][1], dp[i-1][2])
    dp[i][1] = arr[i][1]+min(dp[i-1][0], dp[i-1][2])
    dp[i][2] = arr[i][2]+min(dp[i-1][0], dp[i-1][1])

result = min(dp[K-1][0], dp[K-1][1], dp[K-1][2])
print(result)
