from itertools import permutations

N = int(input())
A = map(int, input().split())

result = []

for perm in permutations(A):
    temp = 0

    for i in range(N-1):
        temp += abs(perm[i] - perm[i+1])

    result.append(temp)

print(max(result))