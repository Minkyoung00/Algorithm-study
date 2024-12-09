def find_origin():
    for i in range(len(supplys)):
        if supplys[i] == 0:
            origin.append(i)


def find_supply(check: int):
    if len(graph[check]) == 0:
        return

    for g in graph[check]:
        if not is_visited[g]:
            is_visited[g] = True
            find_supply(g)


def last_check_supply(check: int):
    if len(graph[check]) == 0:
        return

    for g in graph[check]:
        if is_visited[g]:
            is_visited[g] = False
            last_check_supply(g)


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

origin = []
find_origin()

origin = set(origin)
is_visited = [False] * n
for o in origin:
    is_visited[o] = True

for s in found_supply:
    check = ord(s) - 65

    if is_visited[check] and check not in origin:
        continue

    is_visited[check] = True
    find_supply(check)

for i in range(n):
    if is_visited[i]:
        continue

    last_check_supply(i)

print(n - sum(is_visited))
