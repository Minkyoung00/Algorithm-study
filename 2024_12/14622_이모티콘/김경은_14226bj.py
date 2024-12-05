from collections import deque

s = int(input())
v = [[False] * (s + 1) for _ in range(s + 1)]
q = deque()
q.append([1, 0, 0])
v[1][0] = True

while q:
    screen, clipboard, count = q.popleft()

    if screen == s:
        print(count)
        break

    if screen != clipboard and not v[screen][screen]:
        v[screen][screen] = True
        q.append([screen, screen, count + 1])
    if screen + clipboard <= s and clipboard != 0 and not v[screen + clipboard][clipboard]:
        v[screen + clipboard][clipboard] = True
        q.append([screen + clipboard, clipboard, count + 1])
    if screen != 0 and not v[screen - 1][clipboard]:
        v[screen - 1][clipboard] = True
        q.append([screen - 1, clipboard, count + 1])