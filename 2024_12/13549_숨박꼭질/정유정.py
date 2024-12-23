import sys
from collections import deque

subin, sister = map(int, sys.stdin.readline().strip().split())
queue = deque()
answer = [-1] * 100001
answer[subin] = 0
queue.append(subin)

while queue:
    current = queue.popleft()
    dx = [-1, 1, current]
    for i in range(3):
        mx = current + dx[i]
        if mx < 0 or mx > 100000 or answer[mx] != -1:
            continue

        queue.append(mx)

        if i != 2:
            answer[mx] = answer[current] + 1
        else:
            answer[mx] = answer[current]

print(answer[sister])

