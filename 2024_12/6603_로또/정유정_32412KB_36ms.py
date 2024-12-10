import sys


def back_tracking(idx: int, depth: int):
    if depth == 6:
        print(' '.join(answer))
        return

    for i in range(idx, k):
        if is_visited[i]:
            continue

        is_visited[i] = True
        answer.append(str(nums[i]))
        back_tracking(i, depth + 1)
        is_visited[i] = False
        del answer[-1]


while True:
    array = list(map(int, sys.stdin.readline().split()))
    k = array[0]
    if k == 0:
        break

    nums = array[1:]
    is_visited = [False] * k
    answer = []
    back_tracking(0, 0)
    print()
