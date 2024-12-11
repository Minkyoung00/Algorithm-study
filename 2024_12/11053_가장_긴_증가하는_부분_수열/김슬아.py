import sys
input=sys.stdin.readline
N=int(input())
sequence=list(map(int,input().strip().split()))
length=[1]*(N)
for i in range(N):
    for j in range(i):
        if sequence[j]<sequence[i]:
            if length[j]+1>length[i]:
                length[i]=length[j]+1
print(max(length))
