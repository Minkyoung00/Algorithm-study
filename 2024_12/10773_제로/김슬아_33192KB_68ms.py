import sys
input=sys.stdin.readline
K=int(input())
arr=[]
for _ in range(K):
    element=int(input())
    if element ==0 and len(arr)!=0:
        arr.pop()
    else:
        arr.append(element)

print(sum(arr))
