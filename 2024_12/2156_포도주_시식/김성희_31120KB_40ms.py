import sys
input = sys.stdin.readline

n = int(input())

wine = [0]
for _ in range(n):
	wine.append(int(input()))

dp = [0] * (n+3)
for i in range(1, len(wine)):
	dp[i+2] = max(dp[i+1], dp[i]+wine[i], dp[i-1]+wine[i-1]+wine[i])

print(dp[-1])
