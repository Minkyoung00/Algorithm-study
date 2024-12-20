import sys

size = int(sys.stdin.readline().strip())
signs = list(map(str, sys.stdin.readline().strip().split()))
is_visited = [0 for _ in range(10)]
max_num = -1
min_num = 9999999999
answer = 0


def back_tracking(depth: int):
    global max_num, min_num, answer

    if depth > len(signs):
        if max_num < answer:
            max_num = answer

        if min_num > answer:
            min_num = answer

        return

    for i in range(10):
        if not is_visited[i]:
            is_visited[i] = 1
            prev = answer % 10
            answer = answer * 10 + i

            if depth == 0:
                back_tracking(depth + 1)
            elif compare(prev, i, signs[depth - 1]):
                back_tracking(depth + 1)

            answer //= 10
            is_visited[i] = 0


def compare(a: int, b: int, c: str):
    if c == '<':
        return a < b

    return a > b


back_tracking(0)
print(max_num)
if len(str(min_num)) < size + 1:
    print("0" + str(min_num))
else:
    print(min_num)

