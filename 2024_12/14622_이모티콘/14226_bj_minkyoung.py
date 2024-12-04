from collections import deque

S = int(input())

result = 1000

queue = deque([(1, 1, 1, 0)]) # count(time), unit, sum, pre(0 :copy, 1 :paste, 2 :delete)
visited = set()

while queue:
    count, unit, sum, pre = queue.popleft()

    if (unit, sum, pre) in visited: continue
    visited.add((unit, sum, pre))

    if sum == S:
        result = min(result, count)
        continue
    
    count += 1

    if sum > S: continue

    # 이전 copy
    elif pre == 0:  
        if result == 1000 or result > count:
            queue.append((count, unit, sum + unit, 1))      # paste
            queue.append((count, unit, sum - 1, 2))         # delete

    # 이전 paste OR delete
    else:           
        queue.append((count, sum, sum, 0))                  # copy

        if result == 1000 or result > count: 
            queue.append((count, unit, sum + unit, 1))      # paste
            queue.append((count, unit, sum - 1, 2))         # delete

print(result)