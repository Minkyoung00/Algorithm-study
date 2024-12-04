from collections import deque

S = int(input())

result = []

queue = deque([(1, 1, 1, 0)]) # count, unit, sum, pre(0 :copy, 1 :paste, 2 :delete)
visited = set()

while queue:
    count, unit, sum, pre = queue.popleft()
    count += 1
    
    if (count, unit, sum, pre) in visited:
        continue
    visited.add((count, unit, sum, pre))

    if sum > S: continue

    # 이전 copy
    elif pre == 0:  
        if sum + unit == S:
            result.append(count)
        else:
            if not result or (result and min(result) > count):
                queue.append((count, unit, sum + unit, 1))      # paste

        if sum - 1 == S:
            result.append(count)
        else:
            if not result or (result and min(result) > count):  # delete
                queue.append((count, unit, sum - 1, 2))

    # 이전 paste
    else:           
        queue.append((count, sum, sum, 0))  # copy

        if sum + unit == S:                 # paste
            result.append(count)
        else:
            if not result or (result and min(result) > count):
                queue.append((count, unit, sum + unit, 1)) 

        if sum - 1 == S:
            result.append(count)
        else:
            if not result or (result and min(result) > count):  # delete
                queue.append((count, unit, sum - 1, 2))

print(min(result))