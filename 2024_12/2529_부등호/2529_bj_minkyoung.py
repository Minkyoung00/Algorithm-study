from collections import deque
import sys
input = sys.stdin.readline

k = int(input())
signs = input().split()
queue = deque([(str(i),0) for i in range(10)]) # (이전 수, 부등호 인덱스)
result =[]

while queue:
    pre_nums, sign_i = queue.popleft() # 이전 수, 현재 볼 부등호 인덱스
    pre_n = int(pre_nums[-1])

    if sign_i == k:
        result.append(pre_nums)
        continue

    if signs[sign_i] == '<':
        for i in range(pre_n+1, 10):
            if str(i) not in pre_nums:  
                queue.append((pre_nums + str(i), sign_i + 1))
    else:
        for i in range(0, pre_n):
            if str(i) not in pre_nums:  
                queue.append((pre_nums + str(i), sign_i + 1))

print(result[-1])
print(result[0])
        

