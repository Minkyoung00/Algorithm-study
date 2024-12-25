# 알고리즘 분류보고 힙 써서 다시푼거
import sys
import heapq
input=sys.stdin.readline
n=int(input())
gifts=[]
for _ in range(n):
    nums=list(map(int,input().split()))

    if nums[0]==0:
        if gifts:
            print(-heapq.heappop(gifts))
        else:
            print(-1)
    else:
        for gift in nums[1:]:
            heapq.heappush(gifts,-gift)

# 첫번째 답

import sys
input=sys.stdin.readline
n=int(input())
gifts=[]
for _ in range(n):
    nums=list(map(int,input().split()))

    if nums[0]==0:
        if not gifts:
            print(-1)
        else:
            gifts.sort()
            print(gifts.pop())
    else:
        for i in range(1,nums[0]+1):
            gifts.append(nums[i])
