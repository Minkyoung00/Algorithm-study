n = int(input())
#인접한 모든 자리의 차이가 1인 수를 계단수, 길이가 n
#0부터 9까지 숫자가 모두 등장해야함
mod = 1000000000

#마지막자리수가j고, 비트마스크 상태가 k일때 가능한 계단수
dp = [[0 for _ in range(1<<10)] for i in range(10)]

for i in range(1,10):
    dp[i][1<<i] = 1
    
for i in range(1, n) :
    next = [[0 for _ in range(1024)] for _ in range(10)]
    
    for j in range(10):
        for k in range(1024):
            if j<9:
                next[j][k|(1<<j)] = (next[j][k | (1<<j)] + dp[j+1][k]) % mod
            if j >0:
                next[j][k|(1<<j)] = (next[j][k | (1<<j)] + dp[j-1][k]) % mod
                
    dp = next
print(sum(dp[i][1023] for i in range(10)) % mod)