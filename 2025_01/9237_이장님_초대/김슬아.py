# 정답

import sys

input = sys.stdin.readline

N = int(input())

trees = list(map(int, input().split()))

trees.sort(reverse=True)

max_days = 0
# 각 나무가 심어진 이후 자라는 시간을 계산
# trees[i]= 나무 자라는 데 걸리는 시간 i+1= 나무를 심는 날 (i가 0 부터 시작하기 때문임)
for i in range(N):
    max_days = max(max_days, trees[i] + i + 1)

# 모든 나무가 자란 이후 하루를 더해야 함
result = max_days + 1
print(result)

# 시간초과 내답

import sys

input = sys.stdin.readline

N = int(input())

trees = list(map(int, input().split()))

trees.sort(reverse=True)

tree_max = max(trees)

bowl = list(range(tree_max, tree_max-N, -1))

cnt = 0
while cnt != N:
    for i in range(N):
        if trees[i] > bowl[i]:
            cnt = 0
            for j in range(N):
                bowl[j] += 1
            break
        else:
            cnt += 1

result = 1+bowl[0]+1
print(result)
