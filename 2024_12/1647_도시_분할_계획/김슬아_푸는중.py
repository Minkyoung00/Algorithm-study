N,M=map(int,input().split())
#가중치가 작은 순서대로 연결정보 정렬
graph=sorted([tuple(map(int,input().split())) for _ in range(M)],key=lambda x:x[2])
#range만 써주면 0부터 range 안의 범위까지 쫙 넣어준다.
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
parent=list(range(M+1))
#대표노드를 찾는다
def find(x):
    if parent[x]!=x:
        parent[x]= find(parent[x])
    return parent[x]
#union 어느쪽을 부모로 할 지 결정
for a,b,weight in graph:
    find(a)

print(parent)
print(graph)
