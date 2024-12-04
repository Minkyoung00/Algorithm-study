from collections import deque
S = int(input())
visited = [[-1] * (S+1) for _ in range(S+1)]
q = deque()
q.append((1,0))
visited[1][0] = 0
while q:
    window, clip = q.popleft()
    #복사
    if visited[window][window] == -1:
        visited[window][window] = visited[window][clip] + 1
        q.append((window, window))
    #붙여넣기
    if window + clip <= S and visited[window + clip][clip] == -1:
        visited[window + clip][clip] = visited[window][clip] + 1
        q.append((window + clip, clip))
    
    #삭제
    if window-1 >= 0 and visited[window -1][clip] == -1:
        visited[window-1][clip] = visited[window][clip] + 1
        q.append((window -1, clip))
    
answer = -1
for i in range(S+1):
    if visited[S][i] != -1:
        if answer == -1 or answer > visited[S][i]:
            answer = visited[S][i]
        
print(answer)
