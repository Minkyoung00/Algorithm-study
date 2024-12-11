N = int(input())
A = list(map(int, input().split()))

memo = [(0, 0) for i in range(N)]
max_count = 0

for i in range(N):
    if i == 0:
        memo[i] = (1, A[i])
    else:
        temp = []
        for j in memo[:i]:
            if j[1] < A[i]:
                temp.append(j[0])
        if temp:
            memo[i] = (max(temp)+1, A[i])
        else:
            memo[i] = (1, A[i])
    max_count = max(max_count, memo[i][0])

print(max_count)

