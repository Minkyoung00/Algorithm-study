import sys

nums_size = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().strip().split()))
check_nums = [0 for _ in range(nums_size)]
is_visited = [False for _ in range(nums_size)]

result = 0


def brute_force_search (depth: int):
    global nums_size, result

    if depth == nums_size:
        total = 0
        for i in range(nums_size - 1):
            total += abs(check_nums[i] - check_nums[i + 1])

        result = max(total, result)
        return

    for i in range(nums_size):
        if not is_visited[i]:
            is_visited[i] = True
            check_nums[depth] = nums[i]
            brute_force_search(depth + 1)
            is_visited[i] = False


brute_force_search(0)
print(result)
