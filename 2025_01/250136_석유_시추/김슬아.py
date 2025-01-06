from collections import deque

def solution(land):
    m=len(land[0])
    n=len(land)
    visited=[[0]*m for _ in range(n)]
    queue=deque([(0,0)])
    answer = 0
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    while queue:
        x,y = queue.pop()
        for i in range(4):
            nx=dx[i]+x
            ny=dy[i]+y
            if 0<=nx< m and 0<=ny < n and visited[x][y] == 0 and land[x][y]==1:
                queue.append((nx,ny))
                visited[x][y]=1
    print(visited)
    return answer
