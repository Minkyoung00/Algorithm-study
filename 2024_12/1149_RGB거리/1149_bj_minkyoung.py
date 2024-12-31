N = int(input())
cost = [map(int, input().split()) for i in range(N)]
queue = []

for i in cost:
    