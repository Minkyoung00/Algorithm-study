#dfs 같다
from collections import deque

import sys

input=sys.stdin.readline

N,M = map(int,input().split())
graph= {}
root=set()
edge=set()
visit=set()
for _ in range(M):
    a,b = input().split()
    root.add(a)
    edge.add(b)
    visit.add(a)
    visit.add(b)
    if  a in graph:
        graph[a].append(b)
    else:
        graph[a]=[b]
thiefs= list(input().split())
visited={}
for i in visit:
    visited[i]=False

root=root-edge
cnt=0
def bfs(s):
    queue=deque([s])
    global cnt
    while queue:
        k=queue.popleft()
        visit.remove(k)
        visited[k]=True
        if k in graph:
            for i in graph[k]:
                if not visited[i]:
                    queue.append(i)

for i in range(1,len(thiefs)):
    if thiefs[i] not in root:
        bfs(thiefs[i])
visit=visit-root
print(len(visit))
