def find_origin(check: int):
    global origin

    check_supply = 0
    is_origin = True

    for g in graph:
        if check in g:
            is_origin = False
            break
        check_supply += 1

    if is_origin:
        origin = check
        return

    find_origin(check_supply)


n, m = map(int, input().split())
graph = [[] for _ in range(n)]

for i in range(m):
    supply, demand = input().split()
    graph[ord(supply) - 65].append(ord(demand) - 65)

found_supply = list(input().split())
supply_num = int(found_supply[0])
found_supply = found_supply[1:]

origin = 0
find_origin(0)

is_visited = [False] * n
is_visited[origin] = True
answer = 1


def find_supply(check: int):
    global answer

    if len(graph[check]) == 0:
        return

    for g in graph[check]:
        if not is_visited[g]:
            is_visited[g] = True
            answer += 1
            find_supply(g)


for s in found_supply:
    check = ord(s) - 65
    is_visited[check] = True
    answer += 1
    find_supply(check)

print(n - answer)
