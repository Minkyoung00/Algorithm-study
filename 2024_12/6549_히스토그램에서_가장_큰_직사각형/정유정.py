import sys

while True:
    array = list(map(int, sys.stdin.readline().strip().split()))
    size = array[0] + 1
    if size - 1 == 0:
        break
    heights = [0] + array[1:] + [0]
    stack = []
    max_area = 0

    for i in range(1, size + 1):
        if len(stack) == 0:
            stack.append((i, heights[i]))
            continue
        idx, height = stack.pop()
        if height <= heights[i]:
            stack.append((idx, height))
            stack.append((i, heights[i]))
            continue

        while True:
            max_area = max(max_area, (i - idx) * height)
            if len(stack) != 0:
                idx, height = stack.pop()
                if height <= heights[i]:
                    stack.append((idx, height))
                    stack.append((i, heights[i]))
                    break
            else:
                stack.append((i, heights[i]))
                break

    print(max_area)
