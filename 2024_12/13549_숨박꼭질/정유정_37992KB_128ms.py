import sys
from collections import deque

subin, sister = map(int, sys.stdin.readline().strip().split())
queue = deque()
answer = [-1] * 100001
answer[subin] = 0
queue.append(subin)

while queue:
    current = queue.popleft()

    if 0 <= current * 2 < 100001 and answer[current * 2] == -1:
        answer[current * 2] = answer[current]
        queue.appendleft(current * 2)
    if 0 <= current - 1 < 100001 and answer[current - 1] == -1:
        answer[current - 1] = answer[current] + 1
        queue.append(current - 1)
    if 0 <= current + 1 < 100001 and answer[current + 1] == -1:
        answer[current + 1] = answer[current] + 1
        queue.append(current + 1)

print(answer[sister])
