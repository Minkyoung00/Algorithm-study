import sys
from collections import deque

emoticon_num = int(sys.stdin.readline())
queue = deque()
is_visited = [[False for _ in range(1001)] for _ in range(1001)]
queue.append((1, 0, 0))

while queue:
    monitor, clip_board, time = queue.popleft()
    if monitor == emoticon_num:
        print(time)
        break

    if is_visited[monitor][clip_board]:
        continue

    is_visited[monitor][clip_board] = True

    # copy, subtraction
    if monitor >= 1:
        queue.append((monitor, monitor, time + 1))
        queue.append((monitor - 1, clip_board, time + 1))

    # paste
    if clip_board > 0 and clip_board + monitor <= 1000:
        queue.append((monitor + clip_board, clip_board, time + 1))
