import sys
from collections import deque

computer = int(sys.stdin.readline())
edges = int(sys.stdin.readline())

graph = [[] for _ in range(computer + 1)]

for _ in range(edges):
    vertex1, vertex2, value = map(int, sys.stdin.readline().strip().split())
    graph[vertex1].append((vertex2, value))
    graph[vertex2][vertex1] = value

queue = deque()
queue.append()
