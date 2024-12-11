import sys
input = sys.stdin.readline
while True:
    arr=list(map(int,input().split()))
    if arr[0]==0:
        break
    n=arr[0]
    result=set()
    def solution(s):
        global result
        num_min=float("inf")
        for i in range(s,len(arr)):
            if i==1:
                result.add(arr[i])
                continue
            num_min=min(arr[i],num_min)
            if arr[i-1]<=arr[i]:
                result.add(max(2*arr[i-1],arr[i],num_min*(i+1-s)))
            else:
                result.add(max(arr[i-1],2*arr[i],num_min*(i+1-s)))
    for i in range(1,n+1):
        solution(i)
    print(max(result))
