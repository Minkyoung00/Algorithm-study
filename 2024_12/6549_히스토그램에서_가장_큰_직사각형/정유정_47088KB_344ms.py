import sys

while True:
    graph = list(map(int, sys.stdin.readline().strip().split()))
    if graph[0] == 0:
        break

    stack = []
    max_area = 0

    for i, h in enumerate(graph):
        if i == 0:
            continue

        if stack and stack[-1][1] > h:
            while stack:
                idx, height = stack.pop()
                width_start = 1
                if stack:
                    width_start = stack[-1][0] + 1
                
                max_area = max(max_area, (i - width_start) * height)
                
                if not stack or stack[-1][1] <= h:
                    break
                    
        if not stack or stack[-1][1] <= h:
            stack.append((i, h))

    while stack:
        idx, height = stack.pop()
        width_start = 1
        if stack:
            width_start = stack[-1][0] + 1
    
        max_area = max(max_area, (graph[0] + 1 - width_start) * height)
        
    print(max_area)
