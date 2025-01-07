import sys
input = sys.stdin.readline
N=int(input())
cnt=0
a = N%5
cnt = N//5
while a%3!=0:
    if cnt==0:
        cnt=-1
        break
    cnt-=1
    a =N-5*cnt
if cnt == -1:
    print(-1)
else:
    print((N-5*cnt)//3+cnt)
