N, K = map(int, input().split())
num = [int(i) for i in input()]
result = 0
pre_index = -1

for i in range(N-K):
    max = 0
    for j in range(pre_index + 1, N-K-1+i):
        if max < num[j]:
            max = num[j]
            pre_index = j 
    result += max * 10**(N-K-1-i)

print(result)