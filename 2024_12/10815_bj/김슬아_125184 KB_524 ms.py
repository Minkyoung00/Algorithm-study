#넷째줄을 배열로 받은 뒤 하나씩 둘째줄
# 배열과 확인하면서 일치여부 확인
#dp 문제인가..? 메모이제이션?
#찾아보니 set 함수로 시간복잡도 상수로 줄이면 될듯
import sys
input = sys.stdin.readline
N=int(input())
cards=set(input().split())
M=int(input())
ans=input().split()

for i in range(M):
    if ans[i] in cards:
        ans[i]="1"
    else:
        ans[i]="0"

print(*ans)
