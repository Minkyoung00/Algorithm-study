n = int(input())
arr = []
dp = [0] * (n)
for i in range(n):
    arr.append(list(map(int, input().split())))
    
for j in range(1, n):
    for k in range(j+1):
        if k == 0:
            arr[j][k] += arr[j-1][k]
            
        elif k == j:
            arr[j][k] += arr[j-1][k-1]
        else:
            arr[j][k] += max(arr[j-1][k-1], arr[j-1][k])
            
        
print(max(arr[n-1]))
# for k in arr:
#     print(*k)

    # cnt = max(dp[i+1]+1, dp[i+1]-1)