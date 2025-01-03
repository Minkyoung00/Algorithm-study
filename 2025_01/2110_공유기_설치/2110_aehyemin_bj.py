n, c = map(int, input().split())

x = []

for _ in range(n):
    x.append(int(input()))
    
x.sort()
    
left = 1
right = x[-1] - x[0]

ans = 0

while left <= right:
    mid = (left + right) // 2
    cur = x[0]
    cnt = 1
    
        
    for i in range(1, n):
        if x[i] >= cur + mid :
            cnt += 1
            cur = x[i]
        
    if cnt >= c:
        ans = max(ans, mid)
        left = mid + 1
    else:
        right = mid - 1
            
print(ans)