# 절댓값 abs
from itertools import permutations

N = int(input())
A = list(map(int, input().split()))

max_value = 0

for per in permutations(A):
    cur = sum(abs(per[i]- per[i+1]) for i in range(N-1))
    max_value = max(max_value, cur)
    
print(max_value)