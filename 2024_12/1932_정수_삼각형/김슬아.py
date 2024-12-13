import sys
input= sys.stdin.readline
n=int(input())
trieie=[list(map(int,input().split())) for _ in range(n)]

for i in range(n-2,-1,-1):
    for j in range(i+1):
        trieie[i][j]+=max(trieie[i+1][j],trieie[i+1][j+1])

print(trieie[0][0])
