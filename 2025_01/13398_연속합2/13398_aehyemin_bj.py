n = int(input())
seq = list(map(int, input().split()))
left = [0] * n
right = [0] * n
#seq에서 가장 작은 값은 제거

left[0] = seq[0]
for i in range(1,n):
    left[i] = max(seq[i], left[i-1]+ seq[i])
 
 
right[-1] = seq[-1]   
for i in range(n-2, -1, -1):
    right[i] = max(seq[i], right[i+1] + seq[i])
    
result = max(left)

for i in range(1, n-1):
    result = max(result, left[i-1]+right[i+1])
    
print(result)