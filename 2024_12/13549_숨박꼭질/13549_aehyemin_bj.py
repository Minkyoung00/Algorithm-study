from collections import deque

n, m = map(int, input().split())
check = [0] * 100001
q = deque()

q.append(n)
check[n] = 1

while q:
    x = q.popleft()
    
    if x == m :
        print(check[m]-1)
        break
    
    for nx in (2*x, x-1, x+1):
        if 0 <= nx <= 100000 and check[nx] == 0:
            if nx == 2*x:
                check[nx] = check[x]
                q.append(nx)
                
            else:
                check[nx] = check[x] + 1
                q.append(nx)