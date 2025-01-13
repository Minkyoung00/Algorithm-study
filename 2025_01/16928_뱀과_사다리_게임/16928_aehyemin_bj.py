from collections import deque

n, m = map(int, input().split())

ladder = {}
snake = {}
for i in range(n):
    x, y = map(int,input().split()) #사다리의 정보
    ladder[x] = y
    #x번 칸에 도착하면 y번 칸으로 이동
    
for j in range(m):
    u, v = map(int,input().split()) #뱀의 정보
    snake[u] = v
    #u번 칸에 도착하면, v번 칸으로 이동

def bfs():
    board = list(range(101))
    visited = [0] * 101
    
    for start, end in ladder.items():
        board[start] = end
    for start, end in snake.items():
        board[start] = end

    queue = deque([(1,0)])
    
    while queue:
        pos, cnt = queue.popleft()
        
        if pos == 100:
            return cnt
        
        for dice in range(1,7):
            next_pos = pos + dice
            if next_pos <= 100 and not visited[next_pos]:
                visited[next_pos] = True
                queue.append((board[next_pos], cnt + 1))
            
print(bfs())
#100번 칸에 도착하기 위해 주사위를 몇번 굴려야 하는가?