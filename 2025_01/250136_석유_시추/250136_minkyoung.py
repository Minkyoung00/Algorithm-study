def solution(land):
    n = len(land)       #세로
    m = len(land[0])    #가로
    
    moving = [(1,0),(-1,0),(0,1),(0,-1)]
    visited = [[-1] * m for i in range(n)]

    answer = 0
    fuels = []

    for j in range(m):
        count = 0
        drilled = []
        for i in range(n):
            # 방문을 했는데(확인된 석유덩어리인데) 시추되었다고 표시 안 됨
            if visited[i][j] >= 0 and (visited[i][j] not in drilled):
                count += fuels[visited[i][j]]
                drilled.append(visited[i][j])

            # 방문을 안 했는데 석유가 있는 곳
            if visited[i][j] < 0 and land[i][j]:
                queue = [(i,j)]
                visited[i][j] = len(fuels) # 어떤 석유 덩어리에 포함되는지 표시

                # 새로운 석유 덩어리 조사사
                size = 0
                while queue:
                    cur_y, cur_x = queue.pop()
                    size += 1
                    for x, y in moving:
                        mov_y, mov_x = cur_y+y, cur_x+x
                        if 0 <= mov_x < m and 0 <= mov_y < n and land[mov_y][mov_x] and visited[mov_y][mov_x] < 0:
                            visited[mov_y][mov_x] = len(fuels)
                            queue.append((mov_y,mov_x))

                drilled.append(len(fuels))
                fuels.append(size)
                count += size

        answer = max(answer, count)

    return answer

a = [[1, 0, 1, 0, 1, 1], [1, 0, 1, 0, 0, 0], [1, 0, 1, 0, 0, 1], [1, 0, 0, 1, 0, 0], [1, 0, 0, 1, 0, 1], [1, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1]]
print(solution(a))