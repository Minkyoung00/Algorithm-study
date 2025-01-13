n = int(input())
nums = list(map(int, input().split()))

nagatives_idx = []
nagatives_cnt = 0

for i in range(n):
    if nums[i] < 0:
        nagatives_idx.append(i)
        nagatives_cnt += 1
    
dp = [0] * (nagatives_cnt + 1)

for i in range(nagatives_cnt+1):
    if i  == 0:
        dp[i] = sum(nums[:nagatives_idx[i]])
        continue
    if i == nagatives_cnt:
        if nagatives_idx[i-1] < n-1:
            dp[i] = sum(nums[nagatives_idx[i-1] + 1:])
        continue
    dp[i] = sum(nums[nagatives_idx[i-1]+1:nagatives_idx[i]])

for i in range(nagatives_cnt):
    dp.append(dp[i] + dp[i+1] + nums[nagatives_idx[i]])

print(max(dp))
