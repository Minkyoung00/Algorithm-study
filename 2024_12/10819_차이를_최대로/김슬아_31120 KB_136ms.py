# 브루트포스로 가도 되나?
# permutation을 활용한 모든 경우의 수
import itertools 

N=int(input())
arr=list(map(int,input().split()))
i=0
result=0
for perm in itertools.permutations(arr):
    temp=0
    perm_list = list(perm)
    for i in range(len(perm_list)-1):
        temp += abs(perm_list[i]-perm_list[i+1])
    temp = max(temp,result)
    result=temp

print(result)

# 브루트포스로 가도 되나? 브루트 포스 였음!
# 백트래킹으로 다시 짜기
import sys
input= sys.stdin.readline
N=int(input())
arr=list(map(int,input().split()))
i=0
visited = [False]*len(arr)
pickednum=[]
result=0
def permutation(cnt,depth):
    global result
    if cnt ==depth:
        temp=0
        for i in range(len(pickednum)-1):
            temp += abs(pickednum[i]-pickednum[i+1])
        temp = max(temp,result)
        result =temp
        return
    for index in range(len(arr)):
        if visited[index]==False:
            visited[index]=True
            pickednum.append(arr[index])
            permutation(cnt+1,depth)
            # 백트래킹 하기 위해 되돌림
            pickednum.pop()
            visited[index]=False

permutation(0,len(arr))

print(result)
