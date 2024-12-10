import sys

size = int(sys.stdin.readline()) + 1
nums = [0] + list(map(int, sys.stdin.readline().strip().split()))
dp = [0] * size
pre = 0

for i in range(1, size):
    max_num = 0

    for j in range(1, i):
        if nums[j] < nums[i] and max_num < dp[j]:
            max_num = dp[j]

    dp[i] = max_num + 1

print(max(dp))
