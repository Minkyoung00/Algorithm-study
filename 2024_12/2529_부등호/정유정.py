import sys

size = int(sys.stdin.readline().strip())
signs = list(map(str, sys.stdin.readline().strip().split()))
is_visited = [i for i in range(10)]
max_num = -1
min_answer = 9999999999


def back_tracking(idx: int, depth: int):
    if depth > len(signs):

        return




