while True:
    n = list(map(int, input().split())) #맨 앞이 길이

    number = n[0]
    h = n[1:]
    stack = []
    max_area = 0
    if n[0] == 0:
        break

    for i in range(number):
        if len(stack) == 0:
            stack.append((i, h[i]))
        else:
            if stack[-1][1] < h[i]:
                stack.append((i, h[i]))
            else: # 다음인덱스에서 현재보다 작아졌을때
                while len(stack) > 0 and stack[-1][1] > h[i]:
                    remove = stack.pop()
                    if len(stack) == 0:
                        width = i 
                    else:
                        width = i -  stack[-1][0] - 1
                    max_area = max(max_area, width * remove[1])
                stack.append((i, h[i]))
            
    while stack:
        remove = stack.pop()
        if len(stack) == 0:
            width = number
        else:
            width = number - stack[-1][0] - 1
        max_area = max(max_area, width * remove[1])
    print(max_area)