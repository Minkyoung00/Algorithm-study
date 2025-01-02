n = int(input())
t = list(map(int, input().split()))
    
# 제일 오래걸리는걸 먼저 심기

t.sort(reverse=True)

cnt = 0

for i in range(n):
    cnt = max(cnt, t[i]+ i + 1)

print(cnt+1)
    