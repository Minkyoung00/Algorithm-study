from collections import deque

def solve():
    N, K = map(int, input().split())
    MAX_POS = 100000
    dist = [-1] * (MAX_POS + 1)  # 거리(시간) 정보, -1은 미방문을 의미
    
  
    dq = deque()
    dist[N] = 0
    dq.append(N)
    
    while dq:
        x = dq.popleft()
        
        if x == K:
            print(dist[x])
            return
      
        nx = 2 * x
        if 0 <= nx <= MAX_POS and dist[nx] == -1:
            dist[nx] = dist[x]  # 비용 0 -> 거리(시간) 변화 없음
            dq.appendleft(nx)   # 앞쪽에 삽입하여 우선 탐색

        nx = x - 1
        if 0 <= nx <= MAX_POS and dist[nx] == -1:
            dist[nx] = dist[x] + 1
            dq.append(nx)       # 뒤쪽에 삽입
 
      
        nx = x + 1
        if 0 <= nx <= MAX_POS and dist[nx] == -1:
            dist[nx] = dist[x] + 1
            dq.append(nx)


if __name__ == "__main__":
    solve()