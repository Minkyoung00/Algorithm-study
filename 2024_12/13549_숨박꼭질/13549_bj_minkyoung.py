from collections import deque

N, K = map(int, input().split())

result = []
queue = deque()

if N < K:
    if N == 0 and K > 0:
        N += 1
        queue.append((K, 1)) 
    else:
        queue.append((K, 0)) 
else:
    result.append(N-K)

while queue:
    K, count = queue.popleft()

    while K % 2 == 0 and N < K:
        K //= 2

    if K % 2 != 0 and N < K:
        queue.append((K + 1, count + 1))
        queue.append((K - 1, count + 1))

    if N >= K:
        count += min(N-K, 2*K - N)
        result.append(count)
   
print(min(result))