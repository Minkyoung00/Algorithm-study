def find_supply(check: int):
    if len(graph[check]) == 0:
        return

    for g in graph[check]:
        if not is_visited[g] and chr(g + 65) not in found_supply:
            is_visited[g] = True
            find_supply(g)


n, m = map(int, input().split())
graph = [[] for _ in range(n)]
supplys = [0] * n

for i in range(m):
    supply, demand = input().split()
    graph[ord(supply) - 65].append(ord(demand) - 65)
    supplys[ord(demand) - 65] += 1

found_supply = list(input().split())
supply_num = int(found_supply[0])
found_supply = found_supply[1:]

is_visited = [False] * n
for s in found_supply:
    check = ord(s) - 65
    graph[check].clear()

for i in range(n):
    if not is_visited[i] and supplys[i] == 0:
        find_supply(i)

print(sum(is_visited))
