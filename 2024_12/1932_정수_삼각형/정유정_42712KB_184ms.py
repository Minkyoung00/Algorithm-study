import sys

size = int(sys.stdin.readline())
graph = []
for i in range(size):
    graph.append(list(map(int, sys.stdin.readline().strip().split())))

dp = [[0 for _ in range(size)] for _ in range(size)]
dp[0][0] = graph[0][0]
dx = [0, 1]

for i in range(1, size):
    for j in range(len(graph[i - 1])):
        for x in dx:
            move_x = j + x
            if move_x >= size:
                continue

            dp[i][move_x] = max(dp[i][move_x], graph[i][move_x] + dp[i - 1][j])

print(max(dp[size - 1]))
