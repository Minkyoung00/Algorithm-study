from collections import deque

N,K=map(int,input().split())

queue=deque()

visited=[False]*100001

queue.appendleft((N,0))
def bfs():
    while queue:
        vertex,time=queue.popleft()
        visited[vertex]=True
        if vertex == K:
            return time
        if 0 <= vertex * 2 <= 100000 and not visited[vertex * 2]:
            queue.appendleft((vertex * 2, time))
        if 0 <= vertex - 1 <= 100000 and not visited[vertex - 1]:
            queue.append((vertex - 1, time + 1))
        if 0 <= vertex + 1 <= 100000 and not visited[vertex + 1]:
            queue.append((vertex + 1, time + 1))

print(bfs())
