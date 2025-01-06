def solution(land):
    n = len(land)       #세로
    m = len(land[0])    #가로

    trans_land = list(zip(*land))
    
    moving = [(1,0),(-1,0),(0,1),(0,-1)]
    visited = [[-1] * m for i in range(n)]

    answer = 0
    fuel = [0]*m

    for j in range(m):
        if not trans_land[j]:
            continue
        count = 0

        for i in range(n):
            temp = []
            if visited[i][j] >= 0 and (visited[i][j] not in temp):
                count += fuel[visited[i][j]]
                temp.append(visited[i][j])
            if visited[i][j] < 0 and land[i][j]:
                queue = [(i,j)]
                visited[j][i] = j

                while queue:
                    cur_y, cur_x = queue.pop()
                    count += 1 
                    for x, y in moving:
                        mov_y, mov_x = cur_y+y, cur_x+x
                        if 0 <= mov_x < m and 0 <= mov_y < n and land[mov_y][mov_x] and visited[mov_y][mov_x] < 0:
                            visited[mov_y][mov_x] = j
                            queue.append((mov_y,mov_x))

        fuel[j] = count
        answer = max(answer, count)
    print(fuel)

    return answer

input_v = 	[[1, 0, 1, 0, 1, 1], [1, 0, 1, 0, 0, 0], [1, 0, 1, 0, 0, 1], [1, 0, 0, 1, 0, 0], [1, 0, 0, 1, 0, 1], [1, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1]]
print((solution(input_v)))


    # fuel = []
        
    # for i in range(n):
    #     for j in range(m):
    #         if not visited[i][j] and land[i][j]:
    #             queue = [(i,j)]
    #             count = 0
    #             min_x, max_x = j, j
    #             while queue:
    #                 cur_y, cur_x = queue.pop()
    #                 for x, y in moving:
    #                     mov_y, mov_x = cur_y+y, cur_x+x
    #                     if land[mov_y][mov_x] and not visited[mov_y][mov_x] and  0 <= mov_x <= m and 0 <= mov_y <= n:
    #                         visited[mov_y][mov_x] = True
    #                         min_x = min(min_x, mov_x)
    #                         max_x = max(max_x, mov_x)
    #                         queue.append((mov_y,mov_x))
    #                         count += 1 
    #             fuel.append(count, min_x, max_x)