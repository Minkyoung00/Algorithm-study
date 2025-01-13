from collections import deque

N, M = map(int,input().split())
ladders =  {int(u):int(v) for u, v in (input().split() for i in range(N))}
snakes = {int(u):int(v) for u, v in (input().split() for i in range(M))}

visited = [False] * 101
q = deque([(1,0)])
visited[1] = True

while q:
    pos, cnt = q.popleft()

    if pos == 100:
        print(cnt)
        break
    
    for i in range(1,7):
        new_pos = pos + i
        if new_pos < 101 and not visited[new_pos] :
            if new_pos in ladders:
                new_pos = ladders[new_pos]
            elif new_pos in snakes:
                new_pos = snakes[new_pos]
            
            if not visited[new_pos]:
                visited[new_pos] = True
                q.append((new_pos, cnt+1))