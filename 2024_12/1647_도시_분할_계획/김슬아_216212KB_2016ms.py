#크루스칼 알고리즘을 이용해 mst를 완성한다음 최대 가중치 간선 하나를 제거하는 아이디어
import sys
input=sys.stdin.readline
def find(x):
    if parent[x]!=x:
        parent[x]=find(parent[x])
    return parent[x]
def union(a,b):
    #최종 부모노드로 비교
    a,b=find(a),find(b)
    #이건 내가 구현! a,b를 비교해서 더 작은수로 합친다
    if a<b:
        parent[b]=a
    else:
        parent[a]=b
#정점,간선개수 입력받음
V,E=map(int,input().strip().split())

edges= sorted([tuple(map(int,input().strip().split())) for _ in range(E)], key=lambda x:x[2])
parent=list(range(V+1))
# 최적화 5: mst 리스트 제거, 필요한 정보(총 가중치)만 유지
mst_weight=0
max_weight=0
 # 최적화 6: 조기 종료 조건을 위한 카운터 추가
edge_count=0

for a,b,weight in edges:
    if find(a)!=find(b):
        union(a,b)
        mst_weight+=weight
        max_weight = max(weight,max_weight)
        edge_count+=1
        #최소신장트리 조건:E=V-1# 최적화 6: V-1개의 간선을 선택하면 알고리즘 종료
    if edge_count==V-1:
        break

print(mst_weight-max_weight)
